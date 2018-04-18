
def slack(*args,**kwargs):
    if "message" in kwargs.keys():
        message = kwargs["message"]
    else:
        message = ''
    def decorator(func):
        from slackclient import SlackClient
        import os
        import functools
        slack_token = os.environ["SLACK_API_TOKEN"]
        sc = SlackClient(slack_token)
        @functools.wraps(func)
        def func_wrapper(*args,**kwargs):
            try:
                _return = func(*args,**kwargs)
            except:
                pass
            sc.api_call(
                   "chat.postMessage",
                   channel="@ryan",
                   text="Finished running: {}\n".format(func.__name__)+message
                    )
            return _return
        return func_wrapper
    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    else:
        return decorator

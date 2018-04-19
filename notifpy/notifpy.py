
def slack(*dec_args,**dec_kwargs):
    if "message" in dec_kwargs.keys():
        message = dec_kwargs["message"]
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
            _return = func(*args,**kwargs)
            sc.api_call(
                   "chat.postMessage",
                   channel="@ryan",
                   text="Finished running: {}\n".format(func.__name__)+message
                    )
            return _return
        return func_wrapper
    if len(dec_args) == 1 and callable(dec_args[0]):
        return decorator(dec_args[0])
    else:
        return decorator

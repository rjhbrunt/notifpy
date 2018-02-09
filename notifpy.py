
def email(func):
    def func_wrapper(*args,**kwargs):
        print("Running")
        return func(*args,**kwargs)
    return func_wrapper

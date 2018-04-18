from notifpy import slack
import time

@slack
def m(a,b):
    for i in range(5):
        time.sleep(1)
    return a*b

@slack(message="Hello World")
def some_func():
    return 3+5

if __name__ == "__main__":
    m(2,3)
    some_func()

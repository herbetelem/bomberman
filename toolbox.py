# coding: utf-8

import threading

# FUNCTIONS
# Delay an action
def set_timeout(func, sec):
    """
        Use threading to delay an action. set_timeout(function to delay, how many delay 0.1s = 100ms)
    """

    t = None
    def func_wrapper():
        func()
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return

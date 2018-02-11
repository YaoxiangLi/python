import functools
import time


def timer(func):
    """
    Outputs the time a function takes
    to execute.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)))
        return res
    return wrapper

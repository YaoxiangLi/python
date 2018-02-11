# -*- coding: utf-8 -*-
import time
import functools


# input and output of decorator must be callable
def null_decorator(func):
    return func


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


# syntactic sugar
@null_decorator
@uppercase
def greet():
    return 'hello, daye!'


# greet = null_decorator(greet)
print(greet())


@uppercase
def hello():
    return 'hello, laoban!'


print(hello())


# If the function to be decorated has input parameter
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


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


@timer
def add(nums):
    res = 0
    for num in nums:
        res += num
    return res


print(add([1, 2, 3, 4, 5, 6]))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = fn(*args, **kwargs)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, str((t2 - t1))))
        return res
    return wrapper


# test
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def log2(text=''):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log2('execute')
def f2():
    pass

def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper(g):
    yield from g


def reader_printer(g):
    for v in g:
        print(v)


wrap = reader_wrapper(reader())
for i in wrap:
    print(i)


def writer():
    """A coroutine that writes data *sent* to it to fd, socket, etc."""
    while True:
        w = (yield)
        print('>> ', w)


def writer_wrapper(coro):
    coro.send(None)  # prime the coro
    while True:
        try:
            x = (yield)  # Capture the value that's sent
            coro.send(x)  # and pass it to the writer
        except StopIteration:
            pass


w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # "prime" the coroutine
for i in range(4):
    wrap.send(i)


def double_inputs():
    while True:
        x = yield
        yield x * 2


import inspect

# 协程使用生成器函数定义：定义体中有yield关键字。


def simple_coroutine():
    print('-> coroutine started')    # yield 在表达式中使用；如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式（yield默认返回None）
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()# 和创建生成器的方式一样，调用函数得到生成器对象。
print(inspect.getgeneratorstate(my_coro))
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




















class Stack(object):
    '''
    A python implimentation of stack using list:
    support methods: isEmpty, push, pop, top, size
    '''

    def __init__(self):
        """
        initialize the data in a list.
        """
        self.list = []

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.list == []

    def push(self, input):
        """
        :rtype: void
        """
        self.list.append(input)

    def pop(self):
        return self.list.pop()

    def top(self):
        if self.list == []:
            return None
        else:
            return self.list[len(self.list) - 1]

    def size(self):
        """
        :rtype: int
        """
        return len(self.list)

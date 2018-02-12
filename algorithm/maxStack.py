class MaxStack(object):
    """
    Design a max stack that supports push, pop, top, peekMax and popMax.
    push(x) -- Push element x onto stack.
    pop() -- Remove the element on top of the stack and return it.
    top() -- Get the element on the top.
    peekMax() -- Retrieve the maximum element in the stack.
    popMax() -- Retrieve the maximum element in the stack, and remove it.
    If you find more than one maximum elements, only remove the top-most one.
    """
    def __init__(self):
        """
        initialize the data structure in a list.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.items == []:
            self.items.append((x, x))
        else:
            m = self.items[-1][1]
            if x > m:
                self.items.append((x, x))
            else:
                self.items.append((x, m))

    def pop(self):
        """
        :rtype: void
        """
        if self.items == []:
            return None
        else:
            a = self.items[-1][0]
            self.items.pop()
            return a

    def top(self):
        """
        :rtype: int
        """
        if self.items == []:
            return None
        else:
            return self.items[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        if self.items == []:
            return None
        else:
            return self.items[-1][1]

    def popMax(self):
        if self.items == []:
            return None
        else:
            items2 = []
            m = self.items[-1][1]

            while self.items[-1][0] != m:
                items2.append(self.pop())
            self.items.pop()

            for x in items2[::-1]:
                self.push(x)

            return m


# Test
stack = MaxStack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(9)
stack.push(7)
stack.push(6)
stack.push(4)
print(stack.popMax())

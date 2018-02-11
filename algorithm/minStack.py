class MinStack(object):
    """
    Design a stack that supports push, pop, top,
    and retrieving the minimum element in constant time: O(1).
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    """
    def __init__(self):
        """
        initialize the data in a list.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # check whether the list is empty
        if self.items == []:
            self.items.append((x, x))
        else:
            m = self.items[-1][1]
            if x < m:
                self.items.append((x, x))
            else:
                self.items.append((x, m))

    def pop(self):
        """
        :rtype: int
        """
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

    def getMin(self):
        """
        :rtype: int
        """
        if self.items == []:
            return None
        else:
            return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

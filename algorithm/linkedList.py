class Node(object):
    """Node Class"""
    def __init__(self, data):
        # assign data
        self.data = data
        # initialize next as None
        self.next = None


class LinkedList(object):
    """
    Implementation of LinkedList
    which contains a Node object
    """
    def __init__(self):
        # Initialize head as None
        self.head = None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """
        :type new_data: int
        :rtype: void
        """
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Make next of new Node as head
        new_node.next = self.head
        # Make head pointing to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """
        :type prev_node: Node
        :type new_data: int
        :rtype: void
        """
        # Check if the prev_node exist
        if prev_node is None:
            print('The given previous node does not exist')
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Make new Node pointing to next of prev_node
        new_node.next = prev_node.next
        # Make prev_node pointing to new_node
        prev_node.next = new_node

    def append(self, new_data):
        """
        :type new_data: int
        :rtype: void
        """
        # Instantiated a new Node object
        new_node = Node(new_data)
        # Check if the linkedList is empty
        if self.head is None:
            # If so, make the new_node be the head
            self.head = new_node
        # Else traverse until the last node
        else:
            last = self.head
            while(last.next):
                last = last.next

            # Make the new_node be the last
            last.next = new_node


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printlist()
    llist.push(5)
    llist.printlist()
    llist.insertAfter(llist.head, 9)
    llist.printlist()
    llist.append(10)
    llist.printlist()

"""
    This will contain data structure of Doubly Linked List and basic functions for DLL: 
    The node stores the previous node, the next node, and the element.
"""

class DoublyNode:
    __slots__ = ['data', 'next', 'prev']
    def __init__(self, data):
        """
        Initializes a doubly linked list node.
        :param data: data held by the Node
        :param next: reference to the next Node
        :param prev: reference to the previous Node
        :return: None.
        """
        self.prev = None
        self.next = None
        self.data = data

    def __repr__(self):
        """
        Represents the Node as a string.
        :return: string representation of the Node.
        """
        return f"Node({str(self.data)})"
    __str__ = __repr__


class DoublyLinkedList:
    """
    Implementation of a doubly linked list.
    """

    __slots__ = ["head", "tail", "size"]

    def __init__(self):
        """
        Construct an empty doubly linked list.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        Represent the DLL as a string.
        :return: string representation of the DLL.
        """
        if self.size == 0:
            return 'None'
        current = self.head
        list_str = str(current.data)
        while current.next != None:
            current = current.next
            list_str += "<->" + str(current.data)
        return list_str
    
    def __str__(self):
        """
        Represent the DLL as a string.
        :return: string representation of the DLL.
        """

        return repr(self)
    
    def __sizeof__(self):
        return self.size
    
    def element_by_index(self, index):
        if index < 0 or index > self.size -1:
            return "Index is out of the range"
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, data, back = True):
        """
        Pushs a Node containing val to the head or tail 
        param val, back: value to push
        return: None
        """
        push_node = DoublyNode(data)        # Create new node with data
        if self.size == 0:
            self.head = push_node
            self.tail = push_node
        elif back:
            push_node.prev = self.tail
            self.tail.next = push_node
            self.tail = push_node
        else:
            self.head.prev = push_node
            push_node.next = self.head       # New node to point to old head
            self.head = push_node            # Update the head to new node
        self.size += 1                  # Update the size of the list
        return None
    
    def pop(self, back: bool = True):
        """
        Removes a Node from the back (or front) of the DLL.
        param back: back or front
        return None
        """
        if self.size == 1:
            self.head = None
            self.tail = None
        elif back:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.head.next      # Update head to point the next node
            self.head.prev = None
        self.size -= 1
        return None

    def find(self, data):
        """Looks through the DLL for a node containing 'data'
        :param data: data to search for
        :return: True if found, else False, and the node
        """
        if (self.head == None):
            return False, None
        current_node = self.head
        if (current_node.data == data):
            return True, current_node

        while current_node != self.tail:
            current_node = current_node.next
            if (current_node.data == data):
                return True, current_node
        return False, None

def main():
    test_list = DoublyLinkedList()

    print("Testing doubly linked list implementation")
    option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   F: print the head, tail, and list
                   Q: quit testing \n""")
    while option.lower() != "q":
        if option.lower() == "a":
            print(test_list)
        elif option.lower() == "b":
            elem = input("Enter the element to insert at the head: ")
            test_list.push(elem, False)
        elif option.lower() == "c":
            elem = input("Enter the element to insert at the tail: ")
            test_list.push(elem, True)
        elif option.lower() == "d":
            test_list.pop(False)
        elif option.lower() == "e":
            test_list.pop()
        elif option.lower() == "f":
            print("Head:",test_list.head)
            print("Tail:",test_list.tail)
            print(test_list)

        option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   F: print the head, tail, and list
                   Q: quit testing \n""")
    print("Test Done")
    return None

if __name__ == '__main__':
    main()
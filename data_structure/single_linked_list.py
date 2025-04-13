"""
    This will contain data structure of Single Linked List and basic functions for SLL: 
    The node stores the next node and the element. 
    """

class SLLNode:

    __slots__ = ['data', 'next']
    def __init__(self, data):
        """
            Initializes a SLL Node
            :param data, next
            :return: None
        """
        self.data = data
        self.next = None
    def __str__(self):
        return self.data

class SingleLinkedList:
    """
    SLL implemnetation
    """

    __slot__ = ['head', 'tail', 'size']

    def __init__(self):
        """
        Initializes a SLL
        return: None
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """Represents a SLL as a string
        return: string representation of SLL
        """
        return self.to_string
    
    def __sizeof__(self):
        """ The size of a SLL """
        return self.length()
    
    def __eq__(self, other) -> bool:
        """
        Check if the other single linked list is indentical
        return: True if equal, else False """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)
    
    def element_by_index(self, index):
        if index < 0 or index > self.size -1:
            return "Index is out of the range"
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def is_empty(self):
        return self.size == 0
    
    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of SLL
        """
        current_node = self.head
        result_str =""
        if self.head == None:
            return "None"
        while current_node != self.tail:
            current_str = str(current_node.data)
            result_str += current_str + " --> "
            current_node = current_node.next
        result_str += str(current_node.data)
        return result_str
    
    def append(self, data):
        """
        Append an SLLNode to the end of the SLL
        :param data: data to append
        :return: None
        """
        append_node = SLLNode(data)
        if (self.is_empty()):   #Empty list
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail = append_node
        self.size +=1

        return None
    
    def prepend(self, data):
        """
        Prepend an SLLNode to the head of the SLL
        :param data: data to prepend
        :return: None
        """
        prepend_node = SLLNode(data)
        if (self.is_empty()):   #Empty list
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head = prepend_node

        self.size +=1
        return None
    
    def length(self):
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        return self.size
    
    def remove_head(self):
        """
        Remove the head of the lists
        :return: None
        """
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.next      # Update head to point the next node
            self.size -= 1
    def remove_tail(self):
        """
        Remove the tail of the lists
        :return: None
        """
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            new_tail = self.head
            while new_tail.next != self.tail:
                new_tail = new_tail.next
            new_tail.next = None
            self.tail = new_tail
            self.size -= 1

    def find(self, data):
        """Looks through the SLL for a node containing 'data'
        :param data: data to search for
        :return: True if found, else False
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
    test_list = SingleLinkedList()
    print("Testing single linked list implementation")
    option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   F: print the head, tail, and length
                   Q: quit testing \n""")
    while option.lower() != "q":
        if option.lower() == "a":
            print(test_list)
        elif option.lower() == "b":
            elem = input("Enter the element to insert at the head: ")
            test_list.prepend(elem)
        elif option.lower() == "c":
            elem = input("Enter the element to insert at the tail: ")
            test_list.append(elem)
        elif option.lower() == "d":
            test_list.remove_head()
        elif option.lower() == "e":
            test_list.remove_tail()
        elif option.lower() == "f":
            print("Head:", test_list.head)
            print("Tail:", test_list.tail)
            print("Size of the list:", test_list.length())
        print(test_list)
        option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   F: print the head, tail, and length
                   Q: quit testing \n""")
    print("Test Done")
    return None

if __name__ == '__main__':
    main()
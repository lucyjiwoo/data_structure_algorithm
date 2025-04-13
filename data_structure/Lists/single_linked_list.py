"""
    This will contain data structure of Single Linked List and basic functions for SLL: 
    The node stores the next node and the element. 
    """

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return self.data

class SingleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        if self.size == 0:
            return 'None'
        current = self.head
        list_str = "[" + str(current.data)
        while current.next != None:
            current = current.next
            list_str += ", " + str(current.data)
        list_str += "]"
        return list_str
    def __repr__(self):
        return str(self)
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
    def insert_head(self, data):
        new_node = SLLNode(data)        # Create new node with data
        new_node.next = self.head       # New node to point to old head
        self.head = new_node            # Update the head to new node
        if self.size == 0:
            self.tail = new_node
        self.size += 1                  # Update the size of the list

    def insert_tail(self, data):
        new_tail = SLLNode(data)        #Create new tail node with data
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def remove_head(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.next      # Update head to point the next node
            self.size -= 1
    def remove_tail(self):
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

def main():
    test_list = SingleLinkedList()
    print("Testing single linked list implementation")
    option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   H: print the head
                   T: print the tail
                   Q: quit testing \n""")
    while option.lower() != "q":
        if option.lower() == "a":
            print(test_list)
        elif option.lower() == "b":
            elem = input("Enter the element to insert at the head: ")
            test_list.insert_head(elem)
        elif option.lower() == "c":
            elem = input("Enter the element to insert at the tail: ")
            test_list.insert_tail(elem)
        elif option.lower() == "d":
            test_list.remove_head()
        elif option.lower() == "e":
            test_list.remove_tail()
        elif option.lower() == "h":
            print(test_list.head)
        elif option.lower() == "t":
            print(test_list.tail)

        print(test_list)

        option = input("""Please Enter Your Option
                   A: print all elements of the list in the head to tail order
                   B: insert at the head
                   C: insert at the tail
                   D: remove the head
                   E: remove the tail
                   H: print the head
                   T: print the tail
                   Q: quit testing \n""")
    print("Test Done")
    return 0

if __name__ == '__main__':
    main()
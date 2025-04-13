""" Implement Queue's data structure
    FIFO: First In First Out 
    Enqueue: Adds a new element to the queue.
    Dequeue: Removes and returns the first (front) element from the queue.
    Peek: Returns the first element in the queue.
    isEmpty: Checks if the queue is empty.
    Size: Finds the number of elements in the queue.
    """
from single_linked_list import SLLNode

class Queue:

    def __init__(self):

        self.first = None
        self.last = None
    def __repr__(self):
        return self.to_string()
    
    def to_string(self):
        if self.isEmpty():
            return "Queue is empty"
        result = "IN & OUT | " + str(self.first.data)
        current = self.first
        while current.next != None:
            result += " | " + str(current.next.data)
            current = current.next
        return result
    
    def enqueue(self, element):
        new_node = SLLNode(element)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.first
    
    def isEmpty(self):
        return self.first == None
    
    def size(self):
        size = 0 
        current = self.first
        if current != None:
            size = 1
        else:
            return 0
        while current != self.last:
            size += 1
            current = current.next


q = Queue()
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(3)
print(q)
q.enqueue(4)
print(q)
q.enqueue(5)
print(q)

q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
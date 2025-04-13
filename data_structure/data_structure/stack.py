""" Implement Stack's data structure
    LIFO: Last In First Out 
    """
from doubly_linked_list import DoublyNode

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

class Stack_linked:
    def __init__(self):
        self.top = None
        self.bottom = None
    def __repr__(self):
        return self.to_string()
    
    def to_string(self):
        if self.isEmpty():
            return "Stack is empty"
        result = "TOP\n" + str(self.top.data)
        current = self.top
        while current.prev != None:
            result += "\n" + str(current.prev.data)
            current = current.prev
        return result + "\nBOTTOM"
    
    def push(self, element):
        new_top = DoublyNode(element)
        if self.isEmpty():
            self.top = new_top
            self.bottom = new_top
        else:
            new_top.prev = self.top
            self.top.next = new_top
            self.top = new_top
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        if self.bottom == self.top:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.prev
            self.top.next = None

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top
    
    def isEmpty(self):
        return self.top == None
    
    def size(self):
        size = 0 
        current = self.bottom
        if current != None:
            size = 1
        else:
            return 0
        while current != self.top:
            size += 1
            current = current.next
    

s = Stack_linked()
print(s)

s.push(1)
print(s)

s.push(2)
print(s)

s.push(3)
print(s)

s.push(4)
print(s)

s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

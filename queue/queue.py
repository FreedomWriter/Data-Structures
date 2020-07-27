"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList
from stack import Stack

################# WITH ARRAY #################
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop(0)

################# WITH LINKED LIST #################

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return 
        self.size -= 1
        return self.storage.remove_head()

################# STRETCH #################
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage1 = Stack()
#         self.storage2 = Stack()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # if stack is empty, push the value
#         if self.size == 0:
#             self.storage1.push(value)
#         # if stack is not empty
#         else:
#             # loop through a range equal to the size of the stack
#             for stored in range(self.size):
#                 # empty storage1 and push values to storage2
#                 temp1 = self.storage1.pop()
#                 self.storage2.push(temp1)
#             # push the new value to the front of the queue
#             self.storage1.push(value)

#             # loop and empty storage2 back into storage1 in correct order
#             for stored in range(self.size):
#                 temp2 = self.storage2.pop()
#                 self.storage1.push(temp2)
#         self.size += 1

#     def dequeue(self):
#         if self.size != 0:
#             self.size -= 1
#             return self.storage1.pop()


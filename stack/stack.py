from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.insert(0, value)
#         self.size += 1

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         node = self.storage.pop(0)
#         return node

# new_stack = Stack()
# new_stack.push(2)
# new_stack.push(3)
# new_stack.push(5)
# new_stack.pop()
# print(len(new_stack))

# my_LL = LinkedList()
# my_LL.add_to_head(2)
# my_LL.add_to_tail(4)
# print(my_LL)

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size +=1

    def pop(self):
        if self.size == 0:
            return None
        self.size -=1
        return self.storage.remove_head()
        

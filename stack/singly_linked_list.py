# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node


# class LinkedList:
#     def __init__(self):
#         self.head = None  # Stores a node, that corresponds to our first node in the list
#         self.tail = None  # stores a node tht is the end of the list

#         # return all values for the is a -> b -> c -> d -> None
#     def __str__(self):
#         output = ''
#         # create a tracker variable
#         current_node = self.head

#         # loop until None
#         while current_node is not None:
#             output += f"{current_node.value} -> "
#             # update tracker to next node
#             current_node = current_node.next_node

#         return output

#     def add_to_head(self, value):
#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # new_node should point to current head
#             new_node.next_node = self.head
#             # move head to new_node
#             self.head = new_node

#     def add_to_tail(self, value):
#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # point thendoe at the current tail, to the new node
#             self.tail.next_node = new_node
#             self.tail = new_node


# # remove head and return it's value

#     def remove_head(self):
#         # if list is empty do nothing
#         if not self.head:
#             return None
#         # if list only has one element set head and tail to None
#         if self.head.next_node is None:
#             head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return head_value
#         # otherwise we have more elements in the list
#         else:
#             head_value = self.head.value
#             self.head = self.head.next_node
#             return head_value

#     def contains(self, value):
#         # if self.head is None:
#         #     return False

#         # Loop through each node, until we see the value, or we cannot go further
#         current_node = self.head
#         while current_node is not None:
#             # check if ths is the node we are looking format
#             if current_node.value == value:
#                 return True

#             #otherwise go to the next Node
#             current_node = current_node.next_node
#         #if we exit the loop without finding a value
#         return False

#     def get_max(self):
#         if self.head is None:
#             return None
#         current_node = self.head
#         max_node = self.head.value
#         while current_node is not None:
#             if current_node.value > max_node:
#                 max_node = current_node.value
#             current_node = current_node.next_node
#         return max_node

# linked_list = LinkedList()
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# # print(linked_list.head.value)
# # print(linked_list.tail.value)
# # print(f'does our LLcontain 0? {linked_list.contains(0)}')
# # print(f'does our LLcontain 1? {linked_list.contains(1)}')
# # print(f'does our LLcontain 3? {linked_list.contains(3)}')
# # linked_list.add_to_head(2)
# # print(f'does our LLcontain 2 after adding it to the head? {linked_list.contains(2)}')
# # linked_list.remove_head(2)
# # print(f'does our LLcontain 2 after removing the head? {linked_list.contains(2)}')
# linked_list.add_to_tail(2)
# linked_list.add_to_tail(3)
# print(linked_list)


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.get_value()} -> "
            cur_node = cur_node.get_next()
        return output

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:    
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        # list with one nodes
        elif self.head == self.tail: # this works because we checked to see if the head was None first - if head was None, tail would be None and things would break
            head_value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        # list with 2+ nodes
        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return head_value

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            tail_value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return tail_value
        else:
            tail_value = self.tail
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.length -= 1
            return tail_value

    def contains(self, value):
        if self.head is None and self.tail is None:
            return False
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        #iterate through all the nodes
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max

# my_ll = LinkedList()
# my_ll.add_to_head(2)
# # my_ll.add_to_tail(4)
# # my_ll.add_to_tail(6)
# my_ll.remove_tail()
# # my_ll.remove_head()
# print(my_ll)
# print(my_ll.length)

# print(my_ll.tail)
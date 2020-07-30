"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Queue:
    def __init__(self):
        self.storage = list()

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()


class Stack:
    def __init__(self):
        self.storage = list()

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1 if value is not None else 0

    # Insert the given value into the tree
    def insert(self, value):
        self.size += 1
        if value < self.value:
            # if there is already a value to the left, call insert on self.left
            if self.left:
                return self.left.insert(value)
            else: # there is no value on the left, insert a new node
                self.left = BSTNode(value)
        else: # less than or equal to
            if self.right: # if there is a value on the right, recursively call insert on self.right
                return self.right.insert(value)
            else: # no value on the right, insert a new node
                self.right = BSTNode(value)

    def contains(self, target):
        # if the value is equal to the root value
        if self.value == target:
            return True
        # if the value is greater than the root value and there is a right child - recursively run contains
        elif target > self.value and self.right:
            return self.right.contains(target)
        # if the value is greater than the root value and there is a left child - recursively run contains
        elif target < self.value and self.left:
            return self.right.contains(target)
        # if the value was never found
        return False  

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is a right value
        if self.value and self.right:
            # if the right value is larger than the value - run get_max on self.right
            if self.value < self.right.value:
                return self.right.get_max()
        # if there is only one node
        else:
            return self.value
       
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is None:
            return

        fn(self.value)

        # if there is a left child - run the function on the left child       
        if self.left:
            self.left.for_each(fn)
            
        # if there is a right child - run the function on the right child 
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self is None:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value) # if this moves to the end - everything breaks - WHY?????
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, bst):
        queue = Queue()
        queue.enqueue(bst)
        while queue is not None:
            # remove the first node from the queue
            cur_node = queue.dequeue()
            # print the removed node
            print(cur_node.value)
            # add all children (of removed node) into the queue
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self,bst):
        # create a stack
        stack = Stack()
        # push the bst onto the stack
        stack.push(bst)
        while len(stack.storage) > 0:
            # pop the first item of the stack and store the returned value in current
            current = stack.pop()
            # print the value of current
            print(current.value)
            # if there is a right child, push it onto the stack
            if current.right:
                stack.push(current.right)
            # if there is a left child, push it onto the stack
            if current.left:
                stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, bst):
        while bst is not None:
            # if there is a left child, run dft_print on that left child
            if self.left:
                return self.left.dft_print(self) 
            # if there is a right child, run dft_print on that right child
            if self.right:
                return self.right.dft_print(self)

    # Print Post-order recursive DFT
    def post_order_dft(self, bst):
        if bst: 
    
            # run post_order_dft on the left child 
            self.post_order_dft(bst.left) 
    
            # run post_order_dft on the right child
            self.post_order_dft(bst.right) 
    
            # base case
            print(bst.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("elegant methods")
print("pre order")
bst.pre_order_dft(bst)
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft(bst)  

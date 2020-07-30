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

        
        # start at root and loop until cur_node is None
            # if 'value' <= 'cur_node'
                # if 'cur_node.left' is None
                    # insert our value
                # else 
                    # go left (update 'cur_node' to cur_node.left)
            # elif 'value >= 'cur_node'
                # if 'cur_node.right' is None
                    # insert our value
                # else
                    # go right (update 'cur_node' to cur_node.right)


    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.right.contains(target)
        return False
        # compare 'target' to cur_value
            # 1. == return True
            # 2. < go left
            # 3. > go right
            # t. if can't go left/right (not found, return False)

        
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        # if there is a right value
        if self.value and self.right:
            # if the right value is larger than the value - run get_max on self.right
            if self.value < self.right.value:
                return self.right.get_max()
        else:
            return self.value
       
        # go right until cur_node.right is None\

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is None:
            return

        fn(self.value)
                
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        # cur_node = selffn(cur_node.value)
        # stack = # nodes you need to backtrack to
        # while cur_node.left:
        #     cur_node = cur_node.left
        #     fn(cur_node)
        #     # add it to the stack
        # #pop off the stack
        # # try to go right




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self is None:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # cur_node??????
        # create a queue for nodes
        # add first node to queue
        # while queue is not empty
            # remove the first node from the queue
            # print the removed node
            # add all children (of removed node) into the queue


        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack
        # use same pattern as print_in_order but use the created stack instead of recursion
        # push some initial value(s) onto the stack 
            # push right, root, left, so that the left gets popped last
        # while stack is not empty
            # pop
            # print
            # push
        # done when stack is empty
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

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
# print(bst.in_order_print())
# print(bst.delete(2))
# print(bst.delete(222))

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

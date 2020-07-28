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

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # cur_node = self.value
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
        pass
        # compare 'target' to cur_value
            # 1. == return True
            # 2. < go left
            # 3. > go right
            # t. if can't go left/right (not found, return False)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until cur_node.right is None
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # STRETCH - extra test - write the tests too
    def delete(self, value):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
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

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

"""
Test if a binary tree is height-balanced

A binary tree is said to be height-balanced if for each node in the tree, 
the difference in the height of its left and right subtrees is at most one.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced

Variant 1: Write a program that returns the size of the largest subtree that is complete.

###########################################################################################################

Notes: 
A complete tree is considered complete if all levels are completely filled except 
possibly the last level and last level has all keys as left as possible.

Initial thought was to do BFS - can't do that since the SUBTREE may not be rooted at the initial root node. 
Best alternative is to use DFS method while pushing data to parent node like 9.1

What to send to parent? Basically need to know if a subtree is complete or not, and the size of the subtree


"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class VariantSolution_9_1:
    def dfs_helper(self, root):


    def is_complete(self, root: TreeNode) -> bool:

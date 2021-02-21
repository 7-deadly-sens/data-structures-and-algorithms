"""
Test if a binary tree is height-balanced

A binary tree is said to be height-balanced if for each node in the tree, 
the difference in the height of its left and right subtrees is at most one.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced

Variant 1: Write a program that returns the size of the largest subtree that is complete.

Notes: 
A complete tree is considered 

"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class VariantSolution_9_1:
    def dfs_helper(self, root):


    def is_balanced(self, root: TreeNode) -> bool:
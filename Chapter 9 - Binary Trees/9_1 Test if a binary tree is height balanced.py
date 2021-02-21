"""
Test if a binary tree is height-balanced

A binary tree is said to be height-balanced if for each node in the tree, 
the difference in the height of its left and right subtrees is at most one.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced

Variant 1: Write a program that returns the size of the largest subtree that is complete.

Variant 2: Define a node in a binary tree to be k-balanced if the difference in the number of nodes in left and right subtrees 
is no more than k. Design an algorithm that takes as input a binary tree and positive integer k and returns a node in the binary
tree such that hte node is not k-balanced but all of its descendants are k-balanced. 

For the sake of simplicity - will link to leetcode example for easier testing (https://leetcode.com/problems/balanced-binary-tree/)
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class MainSolution_9_1:

    """
    Bottom Up Approaches
    """
    def dfs_helper(self, root):
        """
        Bottom-up Recursion: 
            Time Complexity: O(N) - each node gets visited once through recursion
            Space Complexity: O(N) - if tree is not balanced/is skewed - then recursion stack will reach number of nodes, N
        """
        if (root is None or self.is_tree_balanced == False):
            return (-1)

        left_height = self.dfs_helper(root.left)
        right_height = self.dfs_helper(root.right)

        curr_height = max(left_height, right_height) + 1
        if (abs(left_height - right_height) > 1):
            self.is_tree_balanced = False
        return(curr_height)

    def is_balanced(self, root: TreeNode) -> bool:
        self.is_tree_balanced = True
        self.dfs_helper(root)
        return(self.is_tree_balanced)

    def dfs_helper(self, root):
        """
        Alternative Way
        """
        if (root is None): return (True, -1)

        is_left_tree_balanced, left_height = dfs_helper(root.left)                      # LEFT
        is_right_tree_balanced, right_height = dfs_helper(root.right)                   # RIGHT

        if (is_right_tree_balanced == False or is_left_tree_balanced == False):         # VISITED
            return(False, max(left_height, right_height))
        
        return(True, max(left_height, right_height) + 1)

    def is_balanced_alt_style(self, root: TreeNode) -> bool:
        """
        Can send an array of values - specifically [is_balanced, BinaryTreeNode]
        """
        self.dfs_helper_alternative(root)
    
    """
    Top Down Approach
    """

    def calculate_height(self, root: TreeNode):
        if (root is None):
            return (-1)
        return (max(self.height(root.left), self.height(root.right)) + 1)
    
    def is_balanced_top_down(self, root: TreeNode):
        """
        Time Complexity: O(N LOG N)
            For the root node, it will calculate the height for the root by going down the left and then the right side.
            Each side will be LOG(N) - height of the tree. So times 2. It will be 2*LOG(N).
            However we call height for each node in the tree and there are N nodes. So it is N * 2 * LOG(N).

            Bounded by O(N) because if the tree is skewed, it will stop recursion as soon as height of a nodes children are not within 1.

        Space Complexity: O(N) - worst case the tree is skewed and it will hold all nodes in the tree in its stack
        """
        if (root is None):
            return True
        
        comparison = abs(self.height(root.left) - self.height(root.right)) <= 1
        ans = comparison and self.is_balanced_top_down(root.left) and self.is_balanced_top_down(root.right)
        return(ans)



"""
Write a program that checks if binary tree is symmetric (e.g. draw a vertical line through the root and the left subtree is a mirror image of the right).

For the sake of simplicity - will link to leetcode example for easier testing (https://leetcode.com/problems/symmetric-tree/)
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recursive_is_symmetric(self, left_tree: TreeNode, right_tree: TreeNode) -> bool:
        if (left_tree is None and right_tree is None):
            return(True)
        if (left_tree is None or right_tree is None):
            return(False)
        if ((left_tree.val == right_tree.val) and \
            (self.recursive_is_symmetric(left_tree.left, right_tree.right) and self.recursive_is_symmetric(left_tree.right, right_tree.left))):
            return(True)
        return(False)


    def is_symmetric(self, root: TreeNode) -> bool:
        """
        Time Complexity: O(N)   -> Visit every node in the tree, N
        Space Complexity: O(N)  -> Worst case, the tree is skewed and so stack recursion is N or number of nodes
                                -> Otherwise, it is O(LOG N) -> height of the binary tree
        """
        return(self.recursive_is_symmetric(root.left, root.right))

    """
    Iterative Approach:
    """
    def is_symmetric_bfs_iterative(self, root: TreeNode) -> bool:
        """
        Iterative approach
        Time complexity: O(N)   -> Visit every node in the tree, N
        Space Complexity: O(M)  -> Length of nodes in the longest row of the binary tree

        """
        # Edge case
        if (root is None): return(True)

        from collections import deque
        q = deque([root.left, root.right])
        while(q):
            first_node = q.popleft()
            second_node = q.popleft()

            if (first_node is None and second_node is None):
                continue
            if (first_node is None or second_node is None):
                return(False)
            if (first_node.val != second_node.val):         # This will check if the values of the binary tree are symmetric (row-wise)
                return(False)
            
            q.extend([first_node.left, second_node.right, first_node.right, second_node.left])
        return(True)




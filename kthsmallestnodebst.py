# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Kth smallest element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
#  of all the values of the nodes in the tree.

class Solution:
    knodeval = 0
    count = 0
    
    def kthSmallestInOrderTraversal(self, root, k):
        if not root:
            return
        
        self.kthSmallestInOrderTraversal(root.left, k)

        self.count += 1
        if self.count == k:
            self.knodeval = root.val
        
        self.kthSmallestInOrderTraversal(root.right, k)
    
    def kthSmallest(self, root, k):
        # inorder traversal gives us the sorted list of node values in a BST
        # we only need to care about the kth smallest value, so we can do it in O(1) space
        self.kthSmallestInOrderTraversal(root, k)
        return self.knodeval
# this problem hasn't been solved yet

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        if root is None:
            return False
        if root.left is not None:
            if root.left.val<=root.val:
                return True
            else:
                return False
        if root.right is not None:
            if root.right.val>=root.val:
                return True
            else:
                return False
        
        return (self.isValidBST(root.left) and self.isValidBST(root.right))
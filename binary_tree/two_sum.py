# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k):
        if root is None:
            return False
        if root.val==k:
            return True
        return self.findTarget(root.left,k-root.val) or self.findTarget(root.right,k-root.val)
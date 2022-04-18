# this problem hasn't been solved yet

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
         
        return self.valid(root,float('-inf'),float('inf'))
    def valid(self,key,lower,upper):
        if key is None:
            return True
        elif lower<key.val<upper:
                return (self.valid(key.left,lower,key.val) and self.valid(key.right,key.val,upper))
        else:
            return False
       
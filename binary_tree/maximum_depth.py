
'''
        3
       / \
      9   20
         /  \
        15   7
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))
        
if __name__ == '__main__':
    
    arr = [3,9,20,None,None,15,7]
    root  = TreeNode(3)
    first = TreeNode(9)
    second = TreeNode(20)
    
    root.left= first
    root.right=  second
    
    forth = TreeNode(15)
    fifth = TreeNode(7)
    second.left =forth
    second.right=fifth
    
    sol = Solution()
    
    print(sol.maxDepth(root))
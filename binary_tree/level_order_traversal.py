# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        
        if root.left is not None and root.right is not None:
            return ([root.left,root.right]+self.levelOrder(root.left)+self.levelOrder(root.right))
        
                
        
        
if __name__ == '__main__':
    root = TreeNode('1')
    node_b = TreeNode('2')
    node_c = TreeNode('3')
    
    root.right = node_b
    node_b.left =node_c
    
    sol  = Solution()
    print(sol.postorderTraversal(root))
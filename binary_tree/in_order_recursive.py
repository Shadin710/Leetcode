class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right))

        
if __name__ == '__main__':
    root = TreeNode('1')
    node_b = TreeNode('2')
    node_c = TreeNode('3')
    
    root.right = node_b
    node_b.left =node_c
    
    sol  = Solution()
    print(sol.inorderTraversal(root))
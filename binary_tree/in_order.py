# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack=[]
        current= root
        in_order = []
        while current or stack: 
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            in_order.append(current.val)
            current = current.right
        return in_order
                


if __name__ == '__main__':
    root = TreeNode('1')
    node_b = TreeNode('2')
    node_c = TreeNode('3')
    
    root.right = node_b
    node_b.left =node_c
    
    sol  = Solution()
    print(sol.inorderTraversal(root))
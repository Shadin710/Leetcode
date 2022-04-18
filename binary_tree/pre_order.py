'''
         a
        / \
       b   c
      /   /
     d   e
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        
        if root is None:
            return []
        stack = [root]
        pre_order_list=[]
        
        while len(stack)>0:
            current = stack.pop()
            pre_order_list.append(current.val)
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)

            
        return pre_order_list
            
if __name__ == '__main__':
    root = TreeNode('1')
    node_b = TreeNode('2')
    node_c = TreeNode('3')
    
    root.right = node_b
    node_b.left =node_c
    
    sol  = Solution()
    print(sol.preorderTraversal(root))
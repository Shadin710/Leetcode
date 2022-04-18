# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        post= []
        while len(stack)>0:
            current = stack[-1]
            
            if current.left ==None and current.right==None:
                post.append(current.val)
                stack.pop()
            else:
                if current.right !=None:
                    stack.append(current.right)
                    current.right=None
                if current.left != None:
                    stack.append(current.left)
                    current.left=None
        return post
if __name__ == '__main__':
    root = TreeNode('1')
    node_b = TreeNode('2')
    node_c = TreeNode('3')
    
    root.right = node_b
    node_b.left =node_c
    
    sol  = Solution()
    print(sol.postorderTraversal(root))
'''
         1
       /  \
      2    2
     / \   / \
    3   4 4   3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return
        root.left ,root.right=root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
if __name__ == '__main__':
    sol =Solution()
    
    root = TreeNode(1)
    second = TreeNode(2)
    third = TreeNode(2)
    forth = TreeNode(3)
    fifth = TreeNode(4)
    sixth = TreeNode(4)
    seventh = TreeNode(3)
    
    root.left= second
    root.right = third
    second.left = forth
    second.right= fifth
    third.left = sixth
    third.right= seventh
    
    print(sol.invertTree(root))
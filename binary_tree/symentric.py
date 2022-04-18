'''
         1
       /  \
      2    2
     / \   / \
    3   4 4   3
'''
'''
    root = TreeNode(1)
    second = TreeNode(2)
    third = TreeNode(2)
    forth = TreeNode(3)
    fifth = TreeNode(4)
    sixth = TreeNode(4)
    seventh = TreeNode(3)
    
    root.left= second
    root.right = third
    
    second.right= forth
   
    third.right= seventh
'''


'''

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

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        stack = [(root.left,root.right)]
        while len(stack)>0:
            current_left,current_right=  stack.pop()
            if current_left is None and current_right is None:
                continue
            if current_left is not None and  current_right is None:
                return False
            if current_left is None and current_right is not None:
                return False
            if current_left.val!=current_right.val:
                return False
            stack.append((current_left.left,current_right.right))
            stack.append((current_left.right,current_right.left))
        return True
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
    
    print(sol.isSymmetric(root))
    
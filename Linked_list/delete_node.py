# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        
        





if __name__ == '__main__':
    sol = Solution()
    first = ListNode(1)
    second= ListNode(2)
    third = ListNode(3)
    forth = ListNode(1)
    first.next = second
    second.next = third
    third.next= forth

    # print(sol.hasCycle(first))
    print(sol.hasCycle(first))
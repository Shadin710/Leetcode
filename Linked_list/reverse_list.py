# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        temp =head
        stack = []
        
        while temp:
            value  =temp.val
            stack.append(value)
            temp = temp.next
        res =None
        for val in stack:
            res = ListNode(val,res)
        return res
        
if __name__ == '__main__':
    sol = Solution()
    first = ListNode(1)
    second= ListNode(2)
    third = ListNode(3)
    forth = ListNode(1)
    first.next = second
    second.next = third
    third.next= forth

    
    print(sol.reverseList(first))
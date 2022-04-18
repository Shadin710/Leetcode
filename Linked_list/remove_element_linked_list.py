# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        temp = dummy= head
        if head is None:
            return head
        while temp.next!=None:
            if temp.next.val ==val:
                temp.next =temp.next.next
            else:
                temp=temp.next
        
        if head.val == val:
            return head.next
        else:
            return head
if __name__ == '__main__':
    sol = Solution()
    res=None
    for i in range(1,5):
        t = 7
        res = ListNode(t,res)
    val= 7
    sol.removeElements(res,val)       
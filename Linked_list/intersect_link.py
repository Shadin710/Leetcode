# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        tempA=headA
        tempB=headB
        
        while tempA and tempB:
            
        
if __name__ == '__main__':
    sol = Solution()
    first = ListNode(4)
    second= ListNode(1)
    third = ListNode(8)
    forth = ListNode(4)
    five = ListNode(5)
    first.next = second
    second.next = third
    third.next= forth
    forth.next = five
    
    first_v1 = ListNode(5)
    second_v1= ListNode(6)
    third_v1 = ListNode(1)
    forth_v1 = ListNode(8)
    five_v1 = ListNode(4)
    six_v1 = ListNode(5)
    first_v1.next = second_v1
    second_v1.next = third_v1
    third_v1.next= forth_v1
    forth_v1.next= five_v1
    five_v1.next= six_v1
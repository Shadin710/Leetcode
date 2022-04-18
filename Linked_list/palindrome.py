# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        temp = dummy = head
        
        stack_og = []
        
        while temp:
            value = temp.val
            stack_og.append(value)
            temp=  temp.next
        ind= len(stack_og)-1
        counter=0
        while dummy:
            val_dummy= dummy.val
            if stack_og[ind]==val_dummy:
                counter+=1
            ind-=1
            dummy= dummy.next
        if counter==len(stack_og):
            return True
        return False
if __name__ == '__main__':
    sol = Solution()
    first = ListNode(1)
    second= ListNode(2)
    third = ListNode(2)
    forth = ListNode(1)
    first.next = second
    second.next = third
    third.next= forth

    
    print(sol.isPalindrome(first))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp  = head
        hash={}
        while temp:
            val = temp.val
            if val not in hash:
                hash[val]=1
            temp = temp.next
        res = None
        key = list(hash.keys())
        key.sort(reverse=True)
        for element in key:
            res = ListNode(element,res)
        return res
        
if __name__ == '__main__':
    
    sol = Solution()
    first=ListNode(1)
    second= ListNode(1)
    third = ListNode(2)
    first.next= second
    second.next= third
    print(sol.deleteDuplicates(first))        
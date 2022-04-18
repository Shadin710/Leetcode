# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        temp  = head
        counter = 1
        odd= []
        even = []
        stack= []
        while temp:            
            stack.append(temp.val)
            temp=temp.next
        result = None
        for element in stack:
            result= ListNode(element,result)
        stack=[]
        while result:
            if counter%2!=0:
                odd.append(result.val)
            else:
                even.append(result.val)
            counter+=1
            result=result.next
        even.extend(odd)
        res=None
        for element in even:
            res=ListNode(element,res)
        while res:
            print(res.val)
            res=res.next
        # return res
        
if __name__ == '__main__':
    sol = Solution()
    res = None
    # arr = [1,4,2,5,3]
    for i in range(1,9):
        res = ListNode(i,res)
    # print(sol.oddEvenList(res))  
    sol.oddEvenList(res)    
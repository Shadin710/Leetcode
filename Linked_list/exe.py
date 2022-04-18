class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
if __name__ == '__main__':
    
    arr =[4,1,2,3]
    for element in arr:
        
        l1 = ListNode(element)
        l1.next = l1
    while l1:
        print(l1.val)
        l1 = l1.next
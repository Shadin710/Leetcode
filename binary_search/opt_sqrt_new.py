class Solution:
    def mySqrt(self, x: int):
        arr= []
        for i in range(46341):
            arr.append(i*i)
        
        start =0
        end = len(arr)-1
        
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]>x:
                end=mid-1
            elif arr[mid]<x:
                start=mid+1
            
        return start-1
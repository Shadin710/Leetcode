class Solution:
    def searchMatrix(self, matrix, target):
        for arr in matrix:
            start = 0
            end= len(arr)-1
            while start<=end:
                mid_point = (start+end)//2
                
                if arr[mid_point]==target:
                    return True
                elif arr[mid_point]>target:
                    end=mid_point-1
                else:
                    start = mid_point+1
        return False
        
        
if __name__=='__main__':
    
    sol=Solution()
    arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target =13
    print(sol.searchMatrix(arr,target))
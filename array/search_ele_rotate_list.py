
class Solution:
    def search(self, nums,target):
        
        start = 0
        end= len(nums)-1
        
        while start<=end:
            mid_point  =(start+end)//2
            
            if nums[mid_point]==target:
                return mid_point 
            
            # left portion
            if nums[start]<=nums[mid_point]:
                if nums[mid_point]<target or nums[start]>target:
                    start=  mid_point+1
                else:
                    end = mid_point-1
            
            # right sorted portion
            else:
                if nums[mid_point]>target or nums[end]<target:
                    end = mid_point-1
                else:
                    start = mid_point+1
        return -1
                
                
                
                
                
if __name__=='__main__':
    
    sol = Solution()
    test_arr=[4,5,6,0,1,2]
    target = 0
    print(sol.search(test_arr,target))
class Solution:
    def search(self, nums, target):
        start  = 0
        end  = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[start]:
                if nums[mid]<target or nums[start]>target:
                    start = mid+1
                else:
                    end=mid-1
            else:
                if nums[end]<target or nums[mid]>target:
                    end= mid-1
                else:
                    start=mid+1
        return -1
if __name__ == '__main__':
    sol = Solution()
    arr =[4,5,6,7,8,1,2,3]
    print(sol.search(arr,8))
                


class Solution:
    def search(self, nums,target):
        
        res_min = nums[0]
        flag=0
        idx_min= 0
        start = 0
        end = len(nums)-1        
        while start<=end:
            
            if nums[start]<nums[end]:
                res_min = min(res_min,nums[start])
                flag=1
                break
            mid_point = (start+end)//2
            
            if res_min >nums[mid_point]:
                res_min = nums[mid_point]
            if nums[mid_point]>=nums[start]:
                start = mid_point+1
            else:
                end= mid_point-1
            idx_min  =mid_point
        return idx_min
        if flag==0:
            left = nums[:idx_min-1]
            right = nums[idx_min:]
            start_left= 0
            end_left= len(left)-1
           
            while start_left<=end_left:
                mid_point_left= (start_left+end_left)//2
               
                if left[mid_point_left]<target:
                    start_left +=1
                elif left[mid_point_left]>target:
                    end_left-=1
                elif left[mid_point_left]==target:
                    return mid_point_left
                
            start_right= 0
            end_right= len(right)-1
            while start_right<=end_right:
                mid_point_right= (start_right+end_right)//2
                not_found_right=0
                if right[mid_point_right]<target:
                    start_right +=1
                elif right[mid_point_right]>target:
                    end_right-=1
                elif right[mid_point_right]==target:
                    return idx_min+mid_point_right
            return -1
        # sorted list
        elif flag==1:
            start = 0
            end =len(nums)-1
            
            while start<=end:
                mid_point = (start+end)//2
                not_found=0
                if nums[mid_point]<target:
                    start+=1
                elif nums[mid_point]>target:
                    end-=1
                elif nums[mid_point]==target:
                    return mid_point
            return -1
                
if __name__=='__main__':
    
    sol = Solution()
    test_arr=[4,5,6,7,0,1,2]
    target = 1
    print(sol.search(test_arr,target))
    
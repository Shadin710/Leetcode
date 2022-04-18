


class Solution:
    def findMin(self, nums):
        res= nums[0]
        start = 0
        end = len(nums)-1
        
        while start<=end:
            
            mid_point = (start+end)//2
            if nums[start]<nums[end]:
                res =  min(res,nums[start])
                break
            
            res  = min(res,nums[mid_point])
            if nums[mid_point]>= nums[start]:
                start = mid_point+1
            else:
                end = mid_point-1
        return res
        
        
if __name__=='__main__':
    
    sol = Solution()
    count_accepted= 0
    count_keys=0
    test_arr=[]
    test = {
        'test 1':[3,4,5,1,2],
        'test 2':[4,5,6,7,0,1,2],
        'test 3':[11,13,15,17],
        'test 4':[9,10,11,2,5],
        'test 5':[4,5,6,1,2,3],
        'test 6':[2,3,1] 
    }
    answer = {
        'test 1':1,
        'test 2':0,
        'test 3':11,
        'test 4':2,
        'test 5':1,
        'test 6':1 
    }
    for key in test.keys():
        get_func= sol.findMin(test[key])
        if answer[key]== get_func:
            count_accepted+=1
        else:
            test_arr.append({key:get_func})
        count_keys+=1
    if count_accepted==count_keys:
        print("Accepted")
    else:
        print("Wrong Answer: ")
        print(test_arr)
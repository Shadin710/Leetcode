class Solution:
    def maxSubArray(self, nums):
        sum_val = 0
        max_arr=[]
        for i in range(len(nums)):
            
            if sum_val<0:
                sum_val=0
            sum_val = sum_val+nums[i]
            max_arr.append(sum_val)
        
        return max(max_arr)
if __name__ == '__main__':
    sol = Solution()
    test ={
        'Test 1': [-2,1,-3,4,-1,2,1,-5,4],
        'Test 2': [5,4,-1,7,8],
        'Test 3': [1],
        'Test 4': [-1]
    }
    for key in test.keys():
        print(sol.maxSubArray(test[key]))
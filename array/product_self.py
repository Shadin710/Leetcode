from cmath import sqrt
import math
class Solution:
    def productExceptSelf(self, nums):
        answer_forward = 1
        answer_backward=1
        product_arr_for=[]
        product_arr_back = []
        answer_arr=[]
        for i in range(len(nums)):
            answer_forward = answer_forward*nums[i]
            product_arr_for.append(answer_forward)
        for i in range(len(nums)-1,-1,-1):
            answer_backward=answer_backward*nums[i]
            product_arr_back.append(answer_backward)
        product_arr_back=product_arr_back[::-1]
        
        for i in range(len(nums)):
            if i==0:
                answer  = 1* product_arr_back[i+1]
            elif i==len(nums)-1:
                answer  = product_arr_for[i-1]* 1
            else:
                answer  = product_arr_for[i-1]* product_arr_back[i+1]
            answer_arr.append(answer)
        
        return answer_arr
if __name__ == '__main__':
    sol = Solution()
    # arr =[1,2,3,4]
    arr={
        'Test: 1':[1,2,3,4],
        'Test: 2':[-1,1,0,-3,3]
    }
    for key in arr.keys():
        print(sol.productExceptSelf(arr[key]))
    # print(sol.productExceptSelf(arr))
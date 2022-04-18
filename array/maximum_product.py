class Solution:
    def maxProduct(self, nums):
        max_product= nums[0]
        mul =1
        for i in range(len(nums)):
            mul = mul*nums[i]
            if mul <=0:
                mul=nums[i]
            max_product = max(max_product,mul)
            
        return max_product
        
if __name__ == '__main__':
    sol = Solution()
    test= {
        '1':[2,3,-2,4], # 6
        '2': [-2,0,-1], # 0
        '3': [1,2,3,4,-1,2], # 24
        '4': [-1], # 0
        '5': [-1,1,2], # 2
        '6': [1,2,3,-2,3,4,5], # 60
        '7':[1,2,3,-2,4,-1,2,7,8],
        '8': [0,2] # 2
    }
    for key in test.keys():
        print(sol.maxProduct(test[key]))
        
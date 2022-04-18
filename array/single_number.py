class Solution:
    def singleNumber(self, nums):
        sum_value=0
        for i in nums:
            sum_value=  sum_value^i
        return sum_value
        # print(single_element)

if __name__=='__main__':
    sol = Solution()
    
    arr=[-1,-1,-12]
    print(sol.singleNumber(arr))
    # sol.singleNumber(arr)
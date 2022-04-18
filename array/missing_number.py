class Solution:
    def missingNumber(self, nums):
        maxi = len(nums)
        sum_list= sum(nums)
        total_sum = (maxi*(maxi+1))//2
        return total_sum-sum_list

if __name__ == '__main__':
    sol = Solution()
    
    arr =[0,1]
    print(sol.missingNumber(arr))
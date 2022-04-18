from itertools import count


class Solution:
    def moveZeroes(self, nums):
        
        length = len(nums)
        count_number = nums.count(0)
        for i in range(count_number):
            nums.remove(0)
            nums.append(0)
        return nums
if __name__ == '__main__':
    sol = Solution()
    
    arr =[0,1,0,3,12]
    print(sol.moveZeroes(arr))
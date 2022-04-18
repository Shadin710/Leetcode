# boyer moore algorithm

class Solution:
    def majorityElement(self, nums):
        length= len(nums)

        count_number=0
        for i in range(length):
            if count_number==0:
                element=nums[i]

            if element ==nums[i]:
                count_number+=1
            elif element!=nums[i]:
                count_number-=1
        return element
if __name__ == '__main__':
    
    sol = Solution()
    nums = [3,2,3]
    print(sol.majorityElement(nums))
    
class Solution:
    def majorityElement(self, nums):
        length= len(nums)
        unique_set = set()
        prev_number=-1
        for i in range(length):
            element = nums[i]
            unique_set.add(element)
            number=0
            for j in range(i,length):
                if element not in unique_set:
                    if element==nums[j]:
                        number+=1
            if number>prev_number:
                prev_number = number
                store_element = element
        return store_element
if __name__ == '__main__':
    
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))
    
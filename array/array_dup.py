class Solution:
    def containsDuplicate(self, nums):
        
        length = len(nums)
        s  = set(nums)
        count_set_element=0
        for i in s:
            count_set_element+=1
        if count_set_element==length:
            return False
        return True
if __name__ == '__main__':
    sol = Solution()
    arr= [1,2,3,4]
    print(sol.containsDuplicate(arr))
        
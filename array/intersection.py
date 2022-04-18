
# this problem hasn't been solved
class Solution:
    def intersect(self, nums1, nums2):
        
        arr = []
        for val in nums1:
            if val in nums2:
                arr.append(val)
        return arr
            

if __name__ == '__main__':
    sol = Solution()
    num1 = [1,2,2,1]
    num2= [2]
    print(sol.intersect(num1,num2))
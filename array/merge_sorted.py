class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        nums1[m:]=nums2
        nums1.sort()
        return nums1
        
if __name__ == '__main__':
    sol = Solution()
    num1 = [1,2,3,0,0,0]
    num2= [2,5,6]
    m= 3
    n= 3
    print(sol.merge(num1,m,num2,n))
        
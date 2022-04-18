class Solution:
    def isPerfectSquare(self, num: int):
        if num==0 or num==1:
            return True
        start=0
        end =num
        while start<=end:
            mid = (start+end)//2
            
            if (mid*mid==num):
                return True
            elif (mid*mid<num):
                start =mid+1
            else:
                end = mid-1
        return False
        
if __name__ == '__main__':
    
    sol = Solution()
    x = 14
    print(sol.isPerfectSquare(x))
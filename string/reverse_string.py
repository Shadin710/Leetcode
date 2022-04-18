class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        return s
if __name__ == '__main__':
    sol = Solution()
    
    arr =["h","e","l","l","o"]
    print(sol.reverseString(arr))
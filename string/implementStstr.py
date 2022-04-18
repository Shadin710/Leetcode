class Solution:
    def strStr(self, haystack: str, needle: str):
        return haystack.find(needle)
    
if __name__ == '__main__':
    sol = Solution()
    haystack= 'aaaaa'
    needle = ''
    print(sol.strStr(haystack,needle))
    
        
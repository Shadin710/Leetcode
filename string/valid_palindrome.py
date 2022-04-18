class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        default_str = 'abcdefghijklmnopqrstuvwxyz'
        default_numbers ='0123456789'
        make_str = ''
        for char in s:
            if char in default_str or char in default_numbers:
                make_str = make_str+char
        return make_str[::-1]==make_str
        
if __name__=='__main__':
    
    sol = Solution()
    s = ' '
    print(sol.isPalindrome(s))
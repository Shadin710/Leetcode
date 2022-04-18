
class Solution:
    def findTheDifference(self, s, t):
        sum_char_s=0
        sum_char_t=0
        for s_element in s:
            sum_char_s +=ord(s_element)
        for t_element in t:
            sum_char_t+=ord(t_element)
        return chr(sum_char_t-sum_char_s)
if __name__ == '__main__':
    sol = Solution()
    
    s = "abcd"
    t = "abcde"
    # print(sol.findTheDifference(s,t))
    print(sol.findTheDifference(s,t))
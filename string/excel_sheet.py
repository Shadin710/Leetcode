class Solution:
    def titleToNumber(self, columnTitle):
        length = len(columnTitle)
        
        sum_len=0
        for i in range(length):
            mul=1
            for j in range(length):
                mul  = mul* 26;
            sum_len = sum_len +mul
            length-=1
        
        return sum_len
if __name__ == '__main__':
    sol = Solution()
    colum = 'ZYF'
    print(sol.titleToNumber(colum))
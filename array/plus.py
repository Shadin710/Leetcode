class Solution:
    def plusOne(self, digits):
        length = len(digits)-1
        
        sum_dig = ''
        
        for i in digits:
            sum_dig+=str(i)
            
        s  = int(sum_dig)+1
        s  = str(s)
        arr=[]
        for i in s:
            arr.append(int(i))
        return arr
        
if __name__ == '__main__':
    
    sol= Solution()
    arr= [9]
    print(sol.plusOne(arr))
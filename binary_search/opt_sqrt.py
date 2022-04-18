class Solution:
    def mySqrt(self, x: int):
        if x==0 or x==1:
            return x
        hash = {}
        for i in range(x):
            if (i*i)>x:
                break
            hash[i*i]=i
        if hash.get(x,-1)==-1:
            key = list(hash.keys())
            start = 0
            end = len(key)-1
            while start<=end:
                mid_point=(start+end)//2
                if key[mid_point]>x:
                    end = mid_point-1
                else:
                    start = mid_point+1
            
            real_val = key[start-1]
            return hash[real_val]
        else:
            return hash[x]
if __name__ == '__main__':
    
    sol = Solution()
    x = 4
    print(sol.mySqrt(x))
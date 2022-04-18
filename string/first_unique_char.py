class Solution:
    def firstUniqChar(self, s: str):
        
        hashmap ={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        idx =0
        for char in s:
            if hashmap[char]<2:
                 return idx
            idx +=1
        return -1
if __name__=='__main__':
    
    sol = Solution()
    s = 'aabb'
    print(sol.firstUniqChar(s))
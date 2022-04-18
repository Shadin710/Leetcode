class Solution:
    def twoSum(self, nums, target):
        hash ={}
        counter=0
        for element in nums:
            hash[element]= counter
            counter+=1
        counter=0
        for element in nums:
            diff =  target -element
            
            if hash.get(diff,-1)!=-1 and counter !=hash.get(diff,-1):
                j = hash[diff]
                return [counter,j]
            counter+=1  

        
if __name__=='__main__':
    sol = Solution()
    arr = [2,7,11,15]
    target = 9
    print(sol.twoSum(arr,target))
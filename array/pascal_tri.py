from numpy import partition


class Solution:
    def generate(self, numRows):
        
        arr = [[1],[1,1]]
        element_arr = []
        for i in range(1,30):
            partition_arr = arr[i]
            element_arr=[]
            element_arr.append(1)
            
            for j in range(len(partition_arr)):

                if j == len(partition_arr)-1:
                    break
                sum_element = partition_arr[j]+partition_arr[j+1]
                
                element_arr.append(sum_element)
            element_arr.append(1)
            
            arr.append(element_arr)
        return arr[:numRows]
if __name__ == '__main__':
    
    sol = Solution()
    numRows=10
    print(sol.generate(numRows))
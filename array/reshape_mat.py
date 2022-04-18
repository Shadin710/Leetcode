# this problem isn't solved

class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        new_arr=[]
        for arr in mat:
            for element in arr:
                new_arr.append(element)
        reshaped_mat_arr = []
        reshaped_mat = []
        idx=0
        if (r*c)<len(new_arr) or (r*c)>len(new_arr):
            return mat
        for i in range(r):
            for j in range(c):
                reshaped_mat_arr.append(new_arr[idx])
                idx+=1
            reshaped_mat.append(reshaped_mat_arr)
        return reshaped_mat

if __name__ == '__main__':
    sol = Solution()
    arr = [[1,2],[3,4]]
    r,c=  1,4
    print(sol.matrixReshape(arr,r,c))
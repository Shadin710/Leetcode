# this problem isn't solved

class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        if len(mat)* len(mat[0])!=r*c:
            return mat
        result = []
        row = []
        for arr in mat:
            for element in arr:
                row.append(element)
                if len(row)==c:
                    result.append(row)
                    break
            row=[]
        return result

if __name__ == '__main__':
    sol = Solution()
    arr = [[1,2],[3,4]]
    r,c=  1,4
    print(sol.matrixReshape(arr,r,c))
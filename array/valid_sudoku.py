
import collections

class Solution:
    def isValidSudoku(self, board):
        row_hash=collections.defaultdict(set)
        counter_column=0
        col_hash=collections.defaultdict(set)
        square_hash=collections.defaultdict(set)
        
        # row check
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in row_hash[r] or board[r][c] in col_hash[c] or board[r][c] in square_hash[(r//3,c//3)]:
                    return False
                row_hash[r].add(board[r][c])
                col_hash[c].add(board[r][c])
                square_hash[(r//3,c//3)].add(board[r][c])
        return True
if __name__ == '__main__':
    
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))
        
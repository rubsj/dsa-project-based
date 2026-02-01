"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_safe(row , col , val):
            # check if value present in row
            if val in board[row]:
                return False
            # check if value present in col
            if val in [board[i][col] for i in range(9)]:
                return False
            # check if val in corresponding 3X3 box
            box_row_start = row - row % 3
            box_col_start = col - col % 3
            for i in range(box_row_start , box_row_start+3):
                for j in range(box_col_start , box_col_start +3):
                    if board[i][j] == val :
                        return False
            return True

        def dfs():
            # find next unfilled cell
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        #found empty cell
                        row , col = i , j 
                        break
                else:
                    continue
                break
            else:
                #all cells are full
                return True

            # look for a number (1..9) that is safe and be feasibily placed in this empty cell
            for num in range(1, 10):
                val = str(num)
                if is_safe(row , col , val):
                    #found a safe value put it on baord
                    board[row][col] = val
                    #recuse to find next unfilled cell
                    if dfs():
                        return True
                    else:
                        board[row][col] = "."
            return False
        dfs()

solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
print(board)

#optimized version with caching
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        def box_id(row , col):
            return (row//3) *3 + (col //3)

        # initialize cache from current board
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    empties.append((r, c))
                else :
                    b = box_id(r, c)
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)

        def is_safe(row , col , val):
            b = box_id(row, col)
            return (val not in rows[row] and val not in cols[col] and val not in boxes[b])

        # k is index into empties
        def dfs(k):
            if k == len(empties):
                return True # all empty cells are filled
            row , col = empties[k]

            # look for a number (1..9) that is safe and be feasibily placed in this empty cell
            for num in range(1, 10):
                val = str(num)
                if is_safe(row , col , val):
                    #found a safe value put it on baord
                    board[row][col] = val
                    b = box_id(row, col)
                    rows[row].add(val)
                    cols[col].add(val)
                    boxes[b].add(val)
                    #recuse to find next unfilled cell
                    if dfs(k+1):
                        return True
                    else:
                        board[row][col] = "."
                        rows[row].remove(val)
                        cols[col].remove(val)
                        boxes[b].remove(val)
            return False
        dfs(0)
        
solution2 = Solution2()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution2.solveSudoku(board)
print(board)
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        input_board = list(range(n))
        res = []
        def convert(nums):
            blist = []
            for num in nums:
                row = ["."]*n
                row[num] = "Q"
                blist.append("".join(row))
            return blist
        def dfs(pos , board):
            # check if diagonal conflict
            # horizontal distal == vertical distance for last queen with every other queen
            for qindex in range(pos-1):
                if (pos-1) -qindex == abs(board[pos-1] - board[qindex]):
                    return
            #base case
            if pos == n :
                print(f"Board Found: {board}")
                res.append(convert(board[:]))
                return
            # recursive case
            for pick in range(pos , n):
                board[pos] , board[pick] = board[pick] , board[pos]
                dfs(pos+1 , board)
                board[pos] , board[pick] = board[pick] , board[pos]
        dfs(0 , input_board)
        return res

# better solution where check for diagonal conflict before sending the work to next level of recursion
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = list(range(n))
        res = []

        # build board does what convert was doing but in python way
        def build_board() -> List[str]:
            return ["." * c + "Q" + "." * (n-c-1) for c in board]

        def is_diag_safe(row: int) -> int :
            # check new queen at (row , board[row]) against all previous rows
            # horizontal distal == vertical distance means diagonal conflict
            c = board[row]
            for r in range(row):
                if row -r  == abs(c -board[r]):
                    return False
            return True

        def dfs(row):
            #base case
            if row == n :
                res.append(build_board())
                return
            # recursive case
            for pick in range(row , n):
                board[row] , board[pick] = board[pick] , board[row]
                if is_diag_safe(row):
                    dfs(row+1)
                board[row] , board[pick] = board[pick] , board[row]
        dfs(0)
        return res
    
# better solution where we build the board row by row and check column and diagonal conflicts using sets
    

solution = Solution1()       
result = solution.solveNQueens(4)
print(result)
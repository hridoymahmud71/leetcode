
# https://leetcode.com/problems/surrounded-regions/
# incomplete ....  :(

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        def traverseDFS(r, c):

            if (r < 1 or r >= rows -1 or c < 1 or c >= cols - 1 or board[r][c] != "O"):
                return
                      
            board[r][c] == "X"

            traverseDFS(r, c-1)  # left
            traverseDFS(r, c+1)  # right
            traverseDFS(r-1, c)  # top
            traverseDFS(r+1, c)  # bottom

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    traverseDFS(r, c)

        return board


# driver code
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
res = sol.numIslands(board)
print("solution is ", res)
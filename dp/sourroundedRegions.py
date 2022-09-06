
# https://leetcode.com/problems/surrounded-regions/
# incomplete ....  :(

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        dp = {}

        def traverseDFS(r, c, dp):
            key = str(r)+"-"+(c)

            if key in dp.keys():
                return dp[key]

            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O"):
                return

            board[r][c] = "-"

            dp[key] =  traverseDFS(r, c-1, dp)  # left
            dp[key] =  traverseDFS(r, c+1, dp)  # right
            dp[key] =  traverseDFS(r-1, c, dp)  # top
            dp[key] =  traverseDFS(r+1, c, dp)  # bottom

        # Mofify the edge "O"s into "-"s
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    traverseDFS(r, c, dp)

        # Flip
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "-":
                    board[r][c] = "O"

        print(board)


# driver code
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
sol = Solution()
res = sol.solve(board)

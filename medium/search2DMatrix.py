# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        def divideAndConquer(r, c):

            current = matrix[r][c]

            if current == None:
                return False
            if current == target:
                return True

            matrix[r][c] = None

            if current > target:
                return (r > 0 and divideAndConquer(r - 1, c)) or (c > 0 and divideAndConquer(r, c - 1))
            else:
                return (r < rows and divideAndConquer(r + 1, c)) or (c < cols and divideAndConquer(r, c + 1))

        return divideAndConquer(0, 0)


# driver code
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5


sol = Solution()
res = sol.searchMatrix(matrix, target)
print("solution is ", res)

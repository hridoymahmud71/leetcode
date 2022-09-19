# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if(image[sr][sc] == color):
            return image

        rows = len(image)
        cols = len(image[0])
        currentColor = image[sr][sc]

        def traverseDFS(r, c):

            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return
                      
            if image[r][c] != currentColor :
                 return

            image[r][c] = color

            traverseDFS(r, c-1)  # left
            traverseDFS(r, c+1)  # right
            traverseDFS(r-1, c)  # top
            traverseDFS(r+1, c)  # bottom

        traverseDFS(sr, sc)

        return image


# driver code
image =  [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol = Solution()
res = sol.floodFill(image, sr, sc, color)
print("solution is ", res)

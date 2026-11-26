# LeetCode - Check if Matrix Is X Matrix
# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        return all(
            (grid[i][j] != 0) if (i == j or i + j == n - 1)
            else (grid[i][j] == 0)
            for i in range(n)
            for j in range(n)
        )

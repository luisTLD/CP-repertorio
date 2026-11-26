# LeetCode - Count Unguarded Cells in the Grid
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in guards: grid[i][j] = 1
        for i, j in walls: grid[i][j] = 2
        for i in range(m):
            active = False
            for j in range(n):
                if grid[i][j] == 1: active = True
                elif grid[i][j] == 2: active = False
                elif active: grid[i][j] = 3
        for i in range(m):
            active = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1: active = True
                elif grid[i][j] == 2: active = False
                elif active: grid[i][j] = 3
        for j in range(n):
            active = False
            for i in range(m):
                if grid[i][j] == 1: active = True
                elif grid[i][j] == 2: active = False
                elif active: grid[i][j] = 3
        for j in range(n):
            active = False
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 1: active = True
                elif grid[i][j] == 2: active = False
                elif active: grid[i][j] = 3
        return sum(row.count(0) for row in grid)

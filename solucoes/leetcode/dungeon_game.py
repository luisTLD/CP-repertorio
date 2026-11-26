# LeetCode - Dungeon Game
# https://leetcode.com/problems/dungeon-game/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        x = len(dungeon)
        y = len(dungeon[0])

        distance = [[float('inf') for _ in range(y+1)] for i in range(x+1)]
        distance[x][y-1] = 1
        distance[x-1][y] = 1

        for i in range(x-1, -1, -1):
            for j in range(y-1, -1, -1):
                minimum_life = min(distance[i+1][j], distance[i][j+1])
                health_needed = minimum_life - dungeon[i][j]

                distance[i][j] = 1 if health_needed <= 0 else health_needed

        return distance[0][0]

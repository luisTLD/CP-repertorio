# LeetCode - The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weak = set()
        res = []

        rows = len(mat)
        cols = len(mat[0])

        for j in range(cols):
            for i in range(rows):
                if i not in weak and mat[i][j] == 0:
                    weak.add(i)
                    res.append(i)

        for i in range(rows):
            if i not in weak:
                res.append(i)

        return res[:k]

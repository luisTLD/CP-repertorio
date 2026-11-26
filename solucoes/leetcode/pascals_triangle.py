# LeetCode - Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resp = [[1]]
        if numRows == 1:
            return resp

        resp.append([1, 1])
        if numRows == 2:
            return resp

        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(resp[i - 1][j] + resp[i - 1][j - 1])
            tmp.append(1)

            resp.append(tmp)

        return resp

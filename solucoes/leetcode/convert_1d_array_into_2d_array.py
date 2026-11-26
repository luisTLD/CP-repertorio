# LeetCode - Convert 1d Array into 2d Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array/
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i*n:(i+1)*n] for i in range(m)]

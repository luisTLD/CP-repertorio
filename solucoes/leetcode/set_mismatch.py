# LeetCode - Set Mismatch
# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        aux = [0] * len(nums)
        for c in nums:
            aux[c-1] += 1
        x = 0
        y = 0
        for i in range(len(aux)):
            if aux[i] == 0:
                x = i+1
            if aux[i] == 2:
                y = i+1
        return [y, x]

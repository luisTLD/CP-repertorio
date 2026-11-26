# LeetCode - Array Partition
# https://leetcode.com/problems/array-partition/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)

        res = 0
        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i+1])

        return res

# LeetCode - Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        res = 0
        average = nums[-1]
        dummy = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > (average / dummy):
                res += 1
            dummy += 1
            average += nums[i]

        return res

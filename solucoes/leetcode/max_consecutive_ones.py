# LeetCode - Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        resp = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                resp = max(resp, count)
                count = 0
        resp = max(resp, count)
        return resp

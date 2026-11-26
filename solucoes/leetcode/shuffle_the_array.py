# LeetCode - Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        resp = []
        i = 0
        while i < n:
            resp.append(nums[i])
            resp.append(nums[i+n])
            i += 1

        return resp

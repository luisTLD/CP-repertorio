# LeetCode - Jump Game
# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]

        for i in range(1, len(nums)):
            if i > reach:
                return False

            reach = max(i + nums[i], reach)

        return True

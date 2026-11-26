# LeetCode - Container with Most Water
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0

        while i < j:
            limit = min(height[i], height[j])
            area = max(area, limit * (j - i))

            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1

        return area

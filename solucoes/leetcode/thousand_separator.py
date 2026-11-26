# LeetCode - Thousand Separator
# https://leetcode.com/problems/thousand-separator/
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")

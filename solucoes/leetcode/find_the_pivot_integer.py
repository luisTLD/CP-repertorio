# LeetCode - Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/
class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = n

        start_sum = self.sum(0, pivot)
        end_sum = self.sum(pivot, n)

        while start_sum > end_sum:
            pivot -= 1

            start_sum = self.sum(0, pivot)
            end_sum = self.sum(pivot, n)

        if start_sum == end_sum:
            return pivot
        return -1

    def sum(self, i: int, j: int) -> int:
        return ((i+j) * ((j-i)+1)) / 2

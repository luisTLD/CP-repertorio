# LeetCode - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, n + m):
            nums1[i] = nums2[j]
            j += 1

        return nums1.sort()

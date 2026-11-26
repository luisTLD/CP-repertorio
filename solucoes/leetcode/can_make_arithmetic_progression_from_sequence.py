# LeetCode - Can Make Arithmetic Progression from Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        arith = False
        diff = arr[1] - arr[0]

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

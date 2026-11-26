# LeetCode - Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self._sumOfLeftLeaves(root, is_left = False)

    def _sumOfLeftLeaves(self, node: Optional[TreeNode], is_left: bool) -> int:
        if node:
            if not node.left and not node.right and is_left:
                return node.val

            left_sum = self._sumOfLeftLeaves(node.left, is_left = True)
            right_sum = self._sumOfLeftLeaves(node.right, is_left = False)

            return left_sum + right_sum
        else:
            return 0

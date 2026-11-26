# LeetCode - Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        num = [1]
        self.foo(root, num, 1)
        return num[0]

    def foo(self, node: Optional[TreeNode], num: List[int], depth: int):
        if node:
            self.foo(node.left, num, depth + 1)
            self.foo(node.right, num, depth + 1)
            if depth > num[0]:
                num[0] = depth

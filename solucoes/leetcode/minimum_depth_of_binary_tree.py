# LeetCode - Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_dep = [0x7FFFFFFFFFFFFFFF]
        self.minDepthRec(root, 1, min_dep)
        return min_dep[0]

    def minDepthRec(self, node: Optional[TreeNode], x: int, min_dep: List[int]):
        if node:
            if not node.left and not node.right:
                min_dep[0] = min(x, min_dep[0])
            else:
                self.minDepthRec(node.left, x + 1, min_dep)
                self.minDepthRec(node.right, x + 1, min_dep)

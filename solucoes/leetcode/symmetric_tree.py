# LeetCode - Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.foo(root.left, root.right)

    def foo(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True
        if not l or not r:
            return False
        return (l.val == r.val) and self.foo(l.left, r.right) and self.foo(l.right, r.left)

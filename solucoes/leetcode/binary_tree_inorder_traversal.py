# LeetCode - Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.foo(root, values)
        return values

    def foo(self, node: Optional[TreeNode], values: List[int]):
        if node:
            self.foo(node.left, values)
            values.append(node.val)
            self.foo(node.right, values)

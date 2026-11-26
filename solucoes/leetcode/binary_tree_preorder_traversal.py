# LeetCode - Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, node: Optional[TreeNode], result: List[int]):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

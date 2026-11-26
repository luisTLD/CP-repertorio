# LeetCode - Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder(root, result)
        return result

    def _postorder(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

# LeetCode - Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_aux = ListNode(0)
        head_aux.next = head

        current = head_aux

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head_aux.next

# LeetCode - Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        new_head = head.next

        aux = head.next
        head.next = aux.next
        aux.next = head

        tmp = head
        head = head.next
        while head is not None and head.next is not None:
            aux = head.next

            head.next = aux.next
            aux.next = head
            tmp.next = aux

            tmp = head
            head = head.next

        return new_head

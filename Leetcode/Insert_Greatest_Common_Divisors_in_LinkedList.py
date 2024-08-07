from typing import Optional
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def computeGreatestCommonDivisor(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.computeGreatestCommonDivisor(b, a % b)

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        new_list_head = ListNode(-1)
        new_list = new_list_head

        while head.next:
            next_node = head.next
            a, b = max(next_node.val, head.val), min(next_node.val, head.val)
            gcd = math.gcd(a, b)

            new_node = ListNode(head.val, ListNode(gcd))
            new_list.next = new_node

            head = head.next
            new_list = new_list.next.next

        new_list.next = ListNode(head.val)

        return new_list_head.next

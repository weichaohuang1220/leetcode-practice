# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        d = ListNode()
        cur = d
        c1 = l1
        c2 = l2
        while c1 or c2 or carry != 0:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            total = v1 + v2 + carry
            remain = total % 10
            carry = total // 10
            cur.next = ListNode(remain)
            cur = cur.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return d.next


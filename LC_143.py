class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        快慢指针找中点
        反转后半部分链表
        合并两个有序链表
        """
        s = head
        f = head
        while f and f.next:
            f = f.next.next
            s = s.next

        cur = s.next
        # 断开链
        s.next = None
        pre = None
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        c1 = head
        c2 = pre
        """
        1 2
        3 4
        1 3 2 4
        c1-> 2
        c2-> 4
        """
        while c1 and c2:
            # 1 3
            tmp1 = c1.next
            tmp2 = c2.next
            c1.next = c2
            c2.next = tmp1
            # 移动到 2 和 4
            c1 = tmp1
            c2 = tmp2






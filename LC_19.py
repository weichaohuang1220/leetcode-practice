class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) -> ListNode:
        """
        f指针走n步
        s和f一起走
        f恰好走到末尾，则s到达待删除节点的前一个
        """
        d = ListNode()
        d.next = head
        f, s = d,d
        for _ in range(n):
            f=f.next
        while f.next:
            s=s.next
            f=f.next
        s.next = s.next.next
        return d.next
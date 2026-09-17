# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head) :
        """
        虚拟头结点 dummy
        p指针：指向 非重复的元素
        p判断p.next and p.next.next相同
            val =p.next.val
            从p的下一个开始跳过重复元素
            while p.next and p.next.val =val
                p.next=p.next.next
        p判断不相同：
                p=p.next
        """
        dummy = ListNode()
        dummy.next = head
        p = dummy

        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                val = p.next.val
                while p.next and p.next.val ==val:
                    p.next =p.next.next
            else:
                p=p.next
        return dummy.next

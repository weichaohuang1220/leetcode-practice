class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def initlist(self, nums):
        dummy=ListNode()
        cur = dummy
        for i in nums:
            cur.next =ListNode(i)
            if __name__ == '__main__':
                cur=cur.next
        return dummy.next

    # n=r - l + 1
    def reverselist(self,head,l ,r):
        n = r - l +1
        dummy = ListNode()
        dummy.next = head
        cur = head
        p = dummy

        for _ in range(l-1):
            cur =cur.next
            p=p.next
        pre = None
        for _ in range(n):
            post = cur.next
            cur.next = pre
            pre =cur
            cur= post
        p.next.next =cur
        p.next =pre
        return dummy.next
if __name__ == '__main__':
    sol = Solution()
    head = sol.initlist([1,2,3,4,5])
    res = sol.reverselist(head,2,4)

    while res:
        print(res.val)
        res= res.next



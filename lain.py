class ListNode:
    def  __init__(self, val = 0, next =None):
        self.val =val
        self.next = next


class Solution:
    def initlist(self,list:[int])-> ListNode:
        d = ListNode(-1)
        cur = d

        for i,c in enumerate(list):
            cur.next=ListNode(c)
            cur=cur.next
        return d.next

    def swap(self, head)-> ListNode:
        L=0
        cur = head
        while cur:
            cur =cur.next
            L+=1
        d = ListNode(-1)
        d.next = head
        p = d
        cur = head

        while L>=2:
            L-=2
            #暂存p
            tail = cur
            pre= None
            for _ in range(2):
                post  = cur.next
                cur.next = pre
                pre =cur
                cur = post
            #拼接反转后尾部
            p.next.next= cur
            #拼接反转后头部
            p.next = pre
            p = tail
        return d.next


if __name__ == '__main__':
    sol =Solution()
    head = sol.initlist([1,2,3,4,5])
    ans = sol.swap(head)

    cur = ans
    while cur:
        print(cur.val)
        cur=cur.next



class Solution:
    def detectCycle(self, head):
        s = head
        f = head 
        pos =-1
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                s= head
                while s!=f:
                    s=s.next
                    f=f.next
                return s

        return None
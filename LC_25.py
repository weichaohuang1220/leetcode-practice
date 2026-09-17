#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Node:
    def __init__(self,val =0, next =None):
        self.next = next
        self.val =val

class Solution:
    def initlist(self, nums):
        d = Node()
        cur = d
        for i in nums:
            cur.next =Node(i)
            cur=cur.next
        return d.next
    def reverse(self,head, k):
        l = 0
        cur = head
        while cur:
            l+=1
            cur=cur.next
        dummy = Node()
        dummy.next = head
        p = dummy
        #pointers move as cur move
        cur =head
        while l>=k:
            l-=k
            p_nxt = p.next
            pre =None
            for _ in range(k):
                post = cur.next
                cur.next = pre
                pre= cur
                cur= post
            #需要在循环外面
            p.next.next = cur
            p.next = pre
            p = p_nxt
        return dummy.next



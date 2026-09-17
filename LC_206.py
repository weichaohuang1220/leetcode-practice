#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Node:
    def __init__(self,val =0, next =None):
        self.val =val
        self.next = next

class Solution:
    def initlist(self, nums):
        dummy = Node()
        cur = dummy

        for i in nums:
            cur.next=Node(i)
            cur=cur.next
        return dummy.next
    def reverse(self, head):
        if not head or head.next is None:
            return head
        cur = head
        pre =None
        while cur:
            post = cur.next
            cur.next = pre
            pre= cur
            cur= post
        return pre


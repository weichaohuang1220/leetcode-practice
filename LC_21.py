#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Node:
    def __init__(self,val=0, next= None):
        self.val =val
        self.next= next
class Solution:
    def merge2list(self,l1, l2):

        dummy = Node()
        cur= dummy
        c1=l1
        c2=l2
        while c1 and c2:
            if c1.val > c2.val:
                cur.next =c2
                c2=c2.next
                cur=cur.next
            else:
                cur.next = c1
                c1=c1.next
                cur = cur.next
        if c1:
            cur.next =c1
        if c2:
            cur.next =c2
        return dummy.next
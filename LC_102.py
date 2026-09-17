#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from collections import deque
class Node:
    def __init__(self,val =0):
        self.val =val
        self.left = None
        self.right = None

class Solution:
    def Levelorder(self, root):
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)

        while q:
            n = len(q)
            path = []
            for i in range(n):
                node = q.popleft()
                path.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(path)
        return res

#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    """
    1.[a,b][c,d]
    L:b > c 合并
    R: max(b,d)
    """
    def mergeInterval(self, intervals):
        intervals.sort(key = lambda x:x[0])
        s[]

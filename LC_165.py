#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from itertools import zip_longest

def compareVersion(self, version1: str, version2: str) -> int:
    a = map(int, version1.split("."))
    b = map(int, version2.split("."))
    """
    map(int, ...)： 把每个字符串转成整数，这样 "01" 变成 1，自动去掉前导零。
    zip_longest(a, b, fillvalue=0)： 
    这是关键。普通 zip 以短的为准，多出来的部分直接丢掉。
    zip_longest 以长的为准，短的那个用 fillvalue 补齐。比如：
    
    a = [1, 2]，b = [1, 2, 0, 0]
    zip 只配对两组：(1,1), (2,2)
    zip_longest(fillvalue=0) 配对四组：(1,1), (2,2), (0,0), (0,0)
    """
    for v1, v2 in zip_longest(a, b, fillvalue=0):
        if v1 != v2:
            return -1 if v1 < v2 else 1
    return 0
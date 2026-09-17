#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#无重复字符的最长子串
"""
滑动窗口：map
如果有重复l移动
"""
class Solution:
    def sol(self, s):
        l = 0
        res =0
        n = len(s)
        from collections import defaultdict
        m = defaultdict(int)
        for r in range(n):
            m[s[r]]+=1
            while m[s[r]] >1:
                m[s[l]]-=1
                l+=1
            res = max(res, r - l + 1)
        return res
if __name__ == '__main__':
    sol = Solution()
    print(sol.sol("pwwkew"))




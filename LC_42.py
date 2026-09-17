#!/usr/bin/env python 
# -*- coding:utf-8 -*-
aclass Solution:
    def trap(self, height: List[int]) -> int:

        """
        bottom:
        单调栈找下一个更大的数字
        弹出其他数字，最后一个数字为h1
        倒数第二个数字为h2 h1-h2
        h1-h2 -bottom[i] * (i - j) 其中i>j
        """
        s =[]#坐标
        ans =0
        for i,h in enumerate(height):
            while s and h >= height[s[-1]]:
                b_idx  = s.pop()
                bh = height[b_idx]

                if not s:
                    break
                h1 = height[s[-1]]
                ht = min(h1,h)- bh
                wd = i - s[-1] -1
                area = ht * wd
                ans+=area
            s.append(i)

        return ans
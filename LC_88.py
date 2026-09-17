#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
思路： nums1 后面有 n 个空位，从后往前填，每次填当前最大的。
三个指针：

p1：nums1 有效部分的末尾（m-1）
p2：nums2 的末尾（n-1）
p：nums1 要填入的位置（m+n-1）

每一步： 比较 nums1[p1] 和 nums2[p2]，大的放到 nums1[p]，对应指针左移。

"""
class Solution:
    def merge(self, nums1, nums2):
        l = len(nums1)
        l2 = len(nums2)

        p1 =l-l2-1
        p2 =l2-1
        p = l+ l2 -1


        while p1>=0 and p2>=0:
            if nums1[p1] < nums2[p2]:
                nums1[p] =nums2[p2]
                p-=1
                p2-=1
            else:
                nums1[p] = nums1[p1]
                p -= 1
                p1-=1

        while p2>=0:
            nums1[p]=nums1[p2]
            p-=1
            p2-=1






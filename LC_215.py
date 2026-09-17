#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from random import randint
"""
第k大元素在排序数组下标为n-k
partition
1.随机选一个数，与[l,r] 中， partition。nums[i]和nums[l]互换 p=nums[l] p_pos= l,l=l+1
l,r分别在p左右两边找， 保证左边小于p,右边大于p;找到则交换 l+=1 r-=1
最后r为p 应该在的位置，r和p_pos对应变量交换，返回r
此时r的左边元素小于r，右边的元素都大于r,返回r

2.piovt =partition(nums,l,r)
find(num,k)
while True
    如果pos == n-k return nums[pos]
    pos > n -k -> r = pos -1 
    pos < n-k -> l = pos+1
    -> pos = partition(l,r)
检查返回的位置
平均时间复杂度O(n)
时间复杂度O(1)
"""
class Solution:

    def findKthlargest(self, nums,k):
        n = len(nums)
        l = 0
        r = n -1
        pos = self.partition(nums,l,r)
        while True:
            if pos < n -k:
                l = pos+1
            elif pos > n- k:
                r = pos -1
            else:
                return nums[pos]
            pos = self.partition(nums, l, r)


    def partition(self, nums,l,r):
        i = randint(l,r)
        nums[l], nums[i] = nums[i],nums[l]
        p = nums[l]
        p_pos = l
        l= l+1
        # n-k
        while l <= r:
            while l<=r and nums[l]<p:
                 l+=1
            while l<=r and nums[r]>p:
                 r-=1
            if l>r:
                 break
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        nums[r],nums[p_pos] = nums[p_pos],nums[r]
        return  r#r为pivot最终的位置




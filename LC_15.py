#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    def threesum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            #从左往右去重
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l =i+1
            r = n-1
            while l <r:
                s = nums[l]+nums[r]
                if s <target:
                    l+=1
                elif s > target:
                    r-=1
                else:
                    res.append([nums[i], nums[l],nums[r]])
                    while l<n-1 and nums[l]==nums[l+1]:
                        l+=1
                    while r>0 and nums[l]==nums[l+1]:
                        r-=1
                    l+=1
                    r-=1
        return  res



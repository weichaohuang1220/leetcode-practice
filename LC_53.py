#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    """
    1.记录前缀和
    2 res=max(当前前缀和-当前最小前缀和, res)
    3.更新最小前缀和
    """
    def maxSubArray(self, nums):
        n = len(nums)
        min_ps = 0
        res= float('-inf')
        s = [0] * (n+1)
        for i in range(n):
            s[i+1] = s[i] + nums[i]
            res = max(res, s[i] - min_ps)
            min_ps = min(s[i+1],min_ps)

        return res
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol =Solution()
    print(sol.maxSubArray(nums))
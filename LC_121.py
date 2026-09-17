#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:

    """
    dp[i]:[0,i]获得股票的最大利润
    维护一个最小价格，初始化为price[i]
    dp = max(dp[i-1],prices[i] - min)
    """
    def maxprofit(self, price):
        n = len(price)
        dp=[0]* n# dp[n-1]前n天最大利润
        min_pirce = price[0]
        for i in range(n):
            dp[i] = max(price[i] - min_pirce, dp[i-1])
            min_pirce = (min_pirce, price[i])
        return dp[n-1]



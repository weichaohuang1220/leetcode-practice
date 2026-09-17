class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i],凑出金额为i的最小硬币数
        dp[0]=0
        其他初始化为inf，
        1.选了5 11- 5 =6， 求=dp[11]=dp[6]+1
        2.选了5 6 -5 =1 求dp[6]=dp[1]+1
        3. 选了1 1 -1 =0 求dp[1] =dp[0]+1
            要在i>=才能更新
        dp[i]=min(dp[i-c]+1,dp[i])
        return dp[n] if ！=inf else -1

        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if i>=c:
                    dp[i]=min(dp[i - c]+1, dp[i])
        return dp[amount] if dp[amount]!=float('inf') else -1
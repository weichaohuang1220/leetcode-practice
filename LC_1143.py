class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j]:text1的前i个字符和text2的前j个字符的公共子序列
        dp[0][0] =0
        比较前i个字符
        字符相同： text1[i]==text2[j] dp[i][j] = dp[i-1][j-1]+1
        字符不同： text1[i]!=text2[j] dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] != text2[j - 1]:  # 前i个字符比较
                    # 不匹配，这俩字符不可能同时出现在公共子序列里，那只能丢掉一个试试：
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return dp[m][n]

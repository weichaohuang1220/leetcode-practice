class Solution:
    """
    dp[i]以nums[i]结尾的最长递增子序列
    nums[i] > nums[j]
    j<i dp[i] = max(dp[j]+1, dp[i])
    """
    def longestIS(self,nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
if __name__ == '__main__':
    a= [1,2,3]
    print(a[::-1])
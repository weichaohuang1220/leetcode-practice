class Solution:
    def editdistance(self,s ,t):
        """
        dp[i][j]=s的前i个字符 -> t的前j个字符的最小操作数
        
        dp[0][j] = j
        dp[i][0] = i
        
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        
        dp[m][n]
        """
        m = len(s)
        n = len(t)
        dp =[['inf'] * (n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j]=j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                   dp[i][j] = dp[i-1][j-1] + 1
                else:
                   dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp [m][n]
    

 
    
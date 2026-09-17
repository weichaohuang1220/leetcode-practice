
class Solution:
    def spiral(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        t,d = 0, m-1
        l,r =0, n-1

        res = [[0]* n for _ in range(m)]
        while t<=d and l<=r:

            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,d+1):
                res.append(matrix[i][r])
            r-=1
            for i in range(r,l-1,-1):
                res.append(matrix[d][i])
            d-=1
            for i in range(d,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res
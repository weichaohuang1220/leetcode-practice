class Solution:
    def generateparetheness(self, n):
        res = []
        def backtrack(path,l,r,n):
            if len(path) == n * 2:
                res.append("".join(path.copy()))
                return

            if l < n:
                path.append("(")
                backtrack(path,l+1,r,n)
                path.pop()
            if r< l:
                path.append(")")
                backtrack(path,l,r+1,n)
                path.pop()

        backtrack([],0,0,n)
        return res


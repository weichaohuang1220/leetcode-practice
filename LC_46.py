class Solution:
    def permutation(self, nums):
        self.n=len(nums)
        used =[False] * self.n
        res =[]
        def backtrack(path):
            if len(path) == self.n:
              res.append(path.copy())
              return


            for i in range(self.n):
              if used[i]:
                  continue
              path.append(nums[i])
              used[i]=True
              backtrack(path)
              used[i]=False
              path.pop()
        backtrack([])
        return res
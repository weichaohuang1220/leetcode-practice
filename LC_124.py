class Soltion:
    def maxPathSum(self, root) -> int:
        self.ans = float('-inf')
        def dfs(node)-> int:
            if not node:
                return 0
            l= max(0,dfs(node.left))
            r= max(0,dfs(node.right))
            self.ans = max(self.ans,node.val + l + r)

            return max(l, r) + node.val
        dfs(root)
        return self.ans
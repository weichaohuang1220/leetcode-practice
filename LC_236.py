from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build(self,nums):
        q= deque()
        root =TreeNode(nums[0])
        i=1
        q.append(root)
        while q:
          node = q.popleft()
          if i< len(nums) and nums[i] is not None:
              node.left = TreeNode(nums[i])
              q.append(node.left)
          i+=1
          if i<len(nums) and nums[i] is not None:
              node.right = TreeNode(nums[i])
              q.append(node.left)
          i+=1
        return  root

    def LCA(self,root, p, q):
        if not root:
            return
        if root == p or root ==q:
            return root
        left= self.LCA(root.left,p,q)
        right= self.LCA(root.right,p,q)

        if left and right:
            return root

        if left is None:
            return right
        if right is None:
            return left






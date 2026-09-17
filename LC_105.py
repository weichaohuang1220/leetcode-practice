# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        """
        1.前序的第pre_l个元素，作为根root, 从中序中找root元素的索引head_i（用map）
        2.中序找到pre_i的位置i,找到左子树的长度left_size = head_i - in_l
        3.root左子树需要的中序:[in_l, head_i-1]
        4.root左子树需要的前序 ； [pre_l+1，pre_l + left_size 左子树长度]
        5.root右子树需要的中序[head_i + 1, in_r]
        6.root右子树需要的前序[pre_l + left_size 左子树长度+1, pre_r]
        7.return root
        8.递归结束：pre_l > pre_r return None 构造空节点


        """
        from collections import defaultdict
        m = defaultdict(int)
        for i,c in enumerate(inorder):
            m[c]=i

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return  None
            root = TreeNode(preorder[pre_l])
            head_i = m[root.val]
            left_size = head_i - in_l
            root.left = build(pre_l+1, pre_l+left_size, in_l,head_i - 1)
            root.right = build(pre_l + left_size +1, pre_r, head_i +1, in_r)

            return root
        return build(0, len(preorder)-1, 0, len(inorder) -1)



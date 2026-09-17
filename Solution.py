class Solution:
    """
第 n 个丑数（Ugly Number II）
定义丑数为只包含质因子 2、3、5 的正整数，且规定 1 是丑数。请设计一个算法返回第 n 个丑数。
示例：
输入: n = 10
输出: 12
解释: 前10个丑数为 [1,2,3,4,5,6,8,9,10,12]
1 *(2 3 5) = 2 3 5
2 *( 2 3 5) 4 6 10
3 * (2 3 5)
1.
      """
    def sol(self, n:int)-> int:
        ans = set()
        base = [2,3,5]
        def backtrack(path, c):
            if  len(path) ==3:
                ans.append(path.copy())
                if len(ans) == n:
                    return
                return
            # 检查len(set)的长度？=n
            # 对每一个传递过来的数分别乘以2,3，5，拿到path
            # 把path放入set中
            # 把path递归调用，每一个元素继续乘以2，3，5
            # 直到set长度达到n



        ""
if __name__ == '__main__':
    sol = Solution()

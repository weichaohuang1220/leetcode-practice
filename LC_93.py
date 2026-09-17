class Solution:
    """
    回溯尝试在每个位置截1~3位作为一段，凑满4段且用完所有字符就收集
    每段合法条件：不超过255、无前导零
    做选择append → 递归 → 撤销pop
    """

    def restoreIpAddresses(self, s: str) -> list[str]:

        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path.copy()))
                return

            # l长度
            for l in range(1, 4):
                if start + l > len(s):
                    break
                num = s[start:start + l]
                if self.isvalid(num):
                    path.append(num)
                    backtrack(start + l, path)
                    path.pop()

        backtrack(0, [])
        return res

    def isvalid(self, num):
        if len(num) > 1 and num[0] == "0":
            return False
        if int(num) > 255:
            return False
        return True



class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        """
        1.carry保证进位
        2.越界就补0
        3.从后往前算
        while 2个字符串长度不同 / 生成的字符串长度比原来长

        """
        n1 = len(num1)
        n2 = len(num2)
        p1 = n1 - 1
        p2 = n2 - 1
        res = []
        while p1 >= 0 or p2 >= 0 or carry != 0:
            x = int(num1[p1]) if p1 >= 0 else 0
            y = int(num2[p2]) if p2 >= 0 else 0
            t = x + y + carry
            carry = t // 10
            remain = t % 10
            res.append(str(remain))
            p1 -= 1
            p2 -= 1
        return "".join(res[::-1])


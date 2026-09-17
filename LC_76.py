from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        滑动窗口: map counter可以比较 ()
        右扩左缩：右指针扩张把字符加入窗口，满足条件后左指针收缩找最小解。
        Counter比较：用 w >= wt 一步判断窗口是否包含目标所有字符，记得删掉 count 为 0 的 key。
        首次特判：res=="" 处理 res 为空的初始情况，之后用长度比较决定是否更新。
        """
        w = Counter()
        wt = Counter(t)
        res=""
        l =0
        for r,c in enumerate(s):
            w[c]+=1
            while w>=wt:
                #not res exclude res =""
                if res == "" or (r -l +1) < len(res):
                    res = s[l:r+1]
                w[s[l]]-=1
                l+=1
        return res
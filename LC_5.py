#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Solution:
    #Bruteforce O(n^3)
        def longestPalindrome(self, s: str) -> str:
            n = len(s)
            m = 0
            max_p = ""
            for i in range(n):
                for j in range(i + 1):
                    stack = []
                    IsPalindromic = True
                    l, r = 0, i
                    while l <= r:
                        if s[l] != s[r]:
                            IsPalindromic = False
                            break
                        l += 1
                        r -= 1
                    if IsPalindromic and (r - l + 1) > m:
                        max_p = s[j::i + 1]
                        m = r - l + 1
            return max_p

        def optimal(self, s):
            """
            对于每一个i，
            形成奇数长度的回文子串 l=i,r =i
            形成偶数长度的回文子串 l=i r=i+1
            最后遍历完的情况是(l,r)双开区间,对于双开区间的有效子串长度是r-l-1,所以要返回[l+1:r]

            :param s:
            :return:
            """
            n = len(s)
            res=""
            for i in range(n):
                l,r = i,i
                while l>=0 and r<n and s[l]==s[r]:
                    l-=1
                    r+=1
                if r-l-1 > len(res):
                    res =s[l+1:r]
                l, r = i, i+1
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(res):
                    res = s[l + 1:r]

            return res

if __name__ == '__main__':
    sol =Solution()
    print(sol.optimal("babad"))
    print(sol.optimal("cbbd"))


# https://leetcode.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        L = len(s)
        dp = {}
        dp[0] = True
        for i in range(1, L + 1):
            for j in range(i):
                if j in dp:
                    if s[j: i] in wordDict:
                        dp[i] = True
                        continue
        return True if L in dp else False

# https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        dp = {len(s): 1}
        for c in range(len(s) - 1, -1, -1):
            if s[c] == '0':
                dp[c] = 0
            else:
                dp[c] = dp[c + 1]
            if (c + 1 < len(s) and 
                ((s[c] == '1') or (s[c] == '2' and s[c + 1] in "0123456"))
            ):
                dp[c] += dp[c + 2]
        return dp[0]

# RECURSIVE APPROACH( A BIT FUZZY ON THIS MYSELF)
# class Solution(object):
#     def numDecodings(self, s):
#         dp = {len(s): 1}

#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             if s[i] == '0':
#                 return 0
#             res = dfs(i + 1)
#             if (( i + 1 < len(s)) and 
#                 ((s[i] == '1') or (s[i] == '2' and s[i+1] in "0123456"))
#             ):
#                 res += dfs(i + 2)
#             dp[i] = res
#             return res
#         return dfs(0)

# https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for target in range(1 , amount + 1):
            for c in coins:
                if target - c >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - c])
        return -1 if dp[amount] == float('inf') else dp[amount]

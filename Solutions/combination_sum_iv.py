# https://leetcode.com/problems/combination-sum-iv/

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for count in range(1, target + 1):
            for num in nums:
                if count >= num:
                    dp[count] += dp[count - num]
        return dp[target]

# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        L = len(nums)
        dp = [1] * L
        for pos in range(L - 1, -1, -1):
            for checked in range(pos + 1, L):
                if nums[pos] < nums[checked]:
                    dp[pos] = max(1 + dp[checked], dp[pos])
        return max(dp)

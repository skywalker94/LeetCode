# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        if not 0 in nums:
            return True
        L = len(nums)
        if L > 1 and nums[0] == 0:
            return False
        if L == 1:
            return True

        dp = [False] * (L)
        dp[L-1] = True
        for i in range(L-1, -1, -1):
            temp = any(dp[x] for x in range(i, min(L, i + nums[i] + 1)))
            dp[i] = temp
        return dp[0]

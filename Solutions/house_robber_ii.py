# https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob_houses(self, nums):
        rob_skip_previous = 0
        rob_previous = 0
        for i in range(len(nums)):
            temp = max(nums[i] + rob_skip_previous, rob_previous)
            rob_skip_previous = rob_previous
            rob_previous = temp
        return rob_previous

    def rob(self, nums):
        return max(self.rob_houses(nums[1:]), self.rob_houses(nums[:-1]), nums[0])

# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        rob_skip_previous = 0
        rob_previous = 0
        for i in range(len(nums)):
            temp = max(nums[i] + rob_skip_previous, rob_previous)
            rob_skip_previous = rob_previous
            rob_previous = temp
        return rob_previous

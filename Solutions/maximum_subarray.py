# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        previous_sum = nums[0]
        for i in range(1, len(nums)):
            previous_sum = max((previous_sum + nums[i]), nums[i])
            max_sum = max(previous_sum, max_sum)
        return max_sum

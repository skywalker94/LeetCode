# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        found = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in found:
                return [found[complement], i]
            found[nums[i]] = i
        return []

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        checked = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in checked:
                return [checked[complement], i]
            checked[nums[i]] = i
        return []

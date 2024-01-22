# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[(len(nums)/2)]

# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        L = len(nums)
        for i in range(L):
            if nums[i] != i:
                return i
        return L

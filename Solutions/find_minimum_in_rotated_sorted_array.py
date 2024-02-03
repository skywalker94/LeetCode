# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        L = len(nums)
        if L == 1:
            return nums[0]
        elif nums[0] < nums[L - 1]:
            return nums[0]
        elif nums[L - 2] > nums[L - 1]:
            return nums[L - 1]
        else:
            if nums[L//2] < nums[0]:
                return self.findMin(nums[:(L//2 + 1)])
            return self.findMin(nums[(L//2):])
        

# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target, start = 0):
        L = len(nums)
        if nums[0] == target:
            return 0 + start
        elif nums[L - 1] == target:
            return L- 1 + start
        elif nums[L//2] == target:
            return L//2 + start
        elif L <= 3:
            return -1

        S = nums[0]
        E = nums[L - 1]
        H = nums[L//2]

        if E > S:
            if target > H:
                start += L//2
                return self.search(nums[(L//2):], target, start) # right half
        elif H < E:
            if (target < E) and (target > H):
                start += L//2
                return self.search(nums[(L//2):], target, start) # right half
        else:
            if (target > H) or (target < E):
                start += L//2
                return self.search(nums[(L//2):], target, start) # right half
        return self.search(nums[:(L//2 + 1)], target, start) # left half

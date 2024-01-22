# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        for n in nums:
            for _ in range(1, nums.count(n)):
                nums.remove(n)
        return len(nums)

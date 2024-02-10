# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution(object):
    def countDistinctIntegers(self, nums):
        nums = list(set(nums))
        for i in range(len(nums)):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))

# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        solutions = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total == 0:
                    solutions.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 # avoid duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 # avoid duplicates

                    left += 1
                    right -= 1
                else:
                    right -= 1

        return solutions

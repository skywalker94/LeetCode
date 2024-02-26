# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [1] * length
        print(answer)
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        right = nums[length-1]
        for i in range(length - 2, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer

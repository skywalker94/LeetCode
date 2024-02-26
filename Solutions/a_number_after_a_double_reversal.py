# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True
        return num % 10 != 0

# # one liner solution
# class Solution(object):
#     def isSameAfterReversals(self, num):
#         return True if num == 0 else num % 10 != 0

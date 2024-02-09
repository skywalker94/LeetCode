# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True
        return num % 10 != 0

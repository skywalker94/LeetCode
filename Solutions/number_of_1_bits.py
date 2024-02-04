# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        ones = 0
        while n:
            ones += n % 2
            n //= 2
        return ones

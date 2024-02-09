# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def within_range(self, n):
        return -2**31 <= n <= 2**31 - 1
    def reverse(self, x):
        new, sign = 0, 1
        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            new = new*10 + x % 10
            x //= 10
        return new * sign if self.within_range(new) else 0

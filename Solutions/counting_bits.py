# https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, n):
        return [str(bin(i)).count('1') for i in range(n+1)]

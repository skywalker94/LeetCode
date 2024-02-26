# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n):
        rev = 0
        bit_length = 32
        for _ in range(bit_length):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev

# https://www.lintcode.com/problem/659/

class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encoded

    def decode(self, str):
        decoded = []
        pos = 0
        for pos in range(len(str)):
            read = pos
            while str[read] != "#":
                j += 1
            length = int(str[pos:read])
            decoded.append(str[read + 1: read + 1 + length])
            pos = read + 1 + length
        return decode

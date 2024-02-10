# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        positive = True
        if s[0] in "-+":
            if s[0] == '-':
                positive = False
            s = s[1:]
        for c in range(len(s)):
            if s[c] not in "1234567890":
                s= s[:c]
                break
        if len(s) == 0:
            return 0
        num = int(s) if positive else int(s) * -1
        num = min(2**31 - 1, num)
        num = max(-2**31, num)
        return num

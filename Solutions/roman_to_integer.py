# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    key = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def parseValue(self, current, next):
        if ((current == 'I' and next in ['V', 'X']) or
            (current == 'X' and next in ['L', 'C']) or
            (current == 'C' and next in ['D', 'M'])
        ):
            return -1 * self.key[current]
        else:
            return self.key[current]

    def romanToInt(self, s):
        value = self.key[s[len(s)-1]]
        for i in range(len(s)-1):
            value += self.parseValue(s[i], s[i+1])
        return value

# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):
    def countSubstrings(self, s):
        L = len(s)
        total = L
        for c in range(L):
            left = c - 1
            right = c + 1
            while left >= 0 and right < L and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            left = c
            right = c + 1
            while left >= 0 and right < L and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
        return total

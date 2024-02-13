# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        max_length = 0
        palindrome = s[0]
        L = len(s)
        for check in range(L):
            left, right = check - 1, check + 1
            while left >= 0 and right < L and s[left] == s[right]:
                if right - left + 1 > max_length:
                    palindrome = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1

            left, right = check, check + 1
            while left >= 0 and right < L and s[left] == s[right]:
                if right - left + 1 > max_length:
                    palindrome = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1
        return palindrome

# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        p = [c for c in s.strip().lower() if c.isalnum()]
        p = ''.join(p)
        return True if p == p[::-1] else False

# Two pointer solution

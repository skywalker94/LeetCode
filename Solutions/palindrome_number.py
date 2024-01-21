# https://leetcode.com/problems/palindrome-number/

# Check the palindrome_number_no_string.py file for the no converting to string approach

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

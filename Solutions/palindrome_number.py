# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

# # not conversion to string approach
# class Solution(object):
#     def isPalindrome(self, x):
#         exponent = 0
#         old = x
#         new = 0
#         while True:
#             new = (new*10) + (x % 10)
#             x = (x - (x% 10)) / 10
#             exponent += 1
#             if (old / 10**exponent) < 1:
#                 break
#         return new == old

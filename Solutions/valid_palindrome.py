# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        p = [c for c in s.strip().lower() if c.isalnum()]
        p = ''.join(p)
        return True if p == p[::-1] else False

# # Two pointer solution
# class Solution(object):
#     def isPalindrome(self, s):
#         s = s.strip().lower()
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             while not s[left].isalnum() and left < right:
#                 left += 1
#             while not s[right].isalnum() and left < right:
#                 right -= 1
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

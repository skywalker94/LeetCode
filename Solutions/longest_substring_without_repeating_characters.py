# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import OrderedDict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_size = 0
        letters = OrderedDict()
        for c in s:
            if c in letters:
                for lett in letters:
                    del letters[lett]
                    if lett == c:
                        break
            letters[c] = True
            max_size = max(max_size, len(letters))
        return max_size

# # For readability
# from collections import OrderedDict
# class Solution(object):
#     def remove_letters(self, letters, char): # done
#         for l in letters:
#             letters.pop(l)
#             if l == char:
#                 break
#         return letters

#     def read_in(self, letters, char):
#         if char not in letters:
#             letters[char] = True
#             return letters
#         letters = self.remove_letters(letters, char)
#         letters[char] = True
#         return letters

#     def lengthOfLongestSubstring(self, s):
#         left = 0
#         max_size = 0
#         letters = OrderedDict()
#         for c in s:
#             letters = self.read_in(letters, c)
#             max_size = max(max_size, len(letters))
#         return max_size

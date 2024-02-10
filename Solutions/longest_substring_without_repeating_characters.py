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

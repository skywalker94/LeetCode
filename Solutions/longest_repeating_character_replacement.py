# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        letters = {}
        for char in set(s):
            letters[char] = 0
        left = 0
        max_length = 1
        for right in range(len(s)):
            letters[s[right]] += 1

            if (right - left + 1) - max(letters.values()) > k:
                letters[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length

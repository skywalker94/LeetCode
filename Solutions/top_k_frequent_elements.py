# https://leetcode.com/problems/top-k-frequent-elements/

from collections import OrderedDict
class Solution(object):
    def topKFrequent(self, nums, k):
        letters = {}
        for n in nums:
            if n in letters:
                letters[n] += 1
            else:
                letters[n] = 1
        letters = OrderedDict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
        return letters.keys()[:k]

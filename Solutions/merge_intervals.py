# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        L = len(intervals)
        if L <= 1:
            return intervals
        result = []
        intervals.sort(key=lambda x:x[0])
        start, end = None, intervals[0][1]
        for i in range(L):
            start = intervals[i][0] if start == None else min(start,intervals[i][0])
            end = max(end, intervals[i][1])
            if i < (L - 1) and end < intervals[i + 1][0]:
                result.append([start, end])
                start = None
            if i == L - 1:
                result.append([start, end])
        return result

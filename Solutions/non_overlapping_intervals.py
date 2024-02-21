# https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[0])
        deleted = 0
        final = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= final:
                final = end
            else:
                deleted += 1
                final = min(end, final)
        return deleted

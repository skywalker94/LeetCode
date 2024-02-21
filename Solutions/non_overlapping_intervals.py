# https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[0])
        deleted = 0
        last_val = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= last_val:
                last_val = end
            else:
                deleted += 1
                last_val = min(end, last_val)
        return deleted

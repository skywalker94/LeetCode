# https://leetcode.com/problems/insert-interval/

class Solution(object):
    def insert(self, intervals, newInterval):
        if intervals == []:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if newInterval[0] <= intervals[0][0] and intervals[-1][1] <= newInterval[1]:
            return [newInterval]
        final_intervals = []
        start_intervals = []
        middle_intervals = []
        for interval in intervals:
            if interval[0] > newInterval[1]:
                final_intervals.append(interval)
            elif interval[1] < newInterval[0]:
                start_intervals.append(interval)
            else:
                middle_intervals.append(interval)
        if middle_intervals == []:
            return start_intervals + [newInterval] + final_intervals
        start = min(middle_intervals[0][0], newInterval[0])
        end = max(middle_intervals[-1][1], newInterval[1])
        return start_intervals + [[start, end]] + final_intervals

# https://leetcode.com/problems/find-median-from-data-stream/

# Dual Heap Solution
# Modified Solution because the sorting was very slow. However this is more memory intensive
import heapq
class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heapq.heappush(self.large, float(num))

        if self.small and self.large and self.large[0] < (-1*self.small[0]):
            heapq.heappush(self.small, (heapq.heappop(self.large) * -1))

        while len(self.small) + 1 < len(self.large):
            heapq.heappush(self.small, (heapq.heappop(self.large) * -1))
        while len(self.large) + 1 <= len(self.small):
            heapq.heappush(self.large, (heapq.heappop(self.small) * -1))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return ((-1*self.small[0]) + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]


# # Sorting solution
# # Initial Solution (intuitive) Very good for memory usage
# class MedianFinder(object):

#     def __init__(self):
#         self.values = []

#     def addNum(self, num):
#         self.values.append(num)

#     def findMedian(self):
#         self.values = sorted(self.values)
#         size = len(self.values)
#         if size % 2 == 0:
#             return float(self.values[size / 2] + self.values[(size/ 2) - 1]) / 2
#         else:
#             return float(self.values[(size - 1 ) / 2])

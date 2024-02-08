# https://leetcode.com/problems/unique-paths/

class Solution(object):
    def combinations(self, total, base):
        top, bottom = 1, 1
        for i in range(base):
            top *= (total - i)
            bottom *= (i + 1)
        return top // bottom
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        elif m <= n:
            return self.combinations(m + n - 2, m - 1)
        return self.combinations(m + n - 2, n - 1)

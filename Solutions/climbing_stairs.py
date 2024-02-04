# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def combinations(self, steps, two_step):
        top, bottom = 1, 1
        for _ in range(two_step):
            top *= (steps - _)
            bottom *= (_ + 1)
        return top // bottom

    def climbStairs(self, n):
        ways, two_step = 1, 1
        while (two_step * 2) <= n:
            ways += self.combinations(n - two_step, two_step)
            two_step += 1
        return ways

# https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        solution_string = ""
        min_length = float('inf')
        target = collections.Counter(t)

        left, right = 0, 0
        T = len(t)
        while right < len(s):
            if s[right] in target:
                target[s[right]] -= 1

            while right - left + 1 >= T and all(instances <= 0 for instances in target.values()):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    solution_string = s[left:right + 1]

                if s[left] in target:
                    target[s[left]] += 1
                left += 1

            right += 1

        return solution_string

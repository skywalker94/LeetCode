# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        mirror = {']': '[', '}': '{', ')': '('}
        brackets = []
        for c in s:
            if c in set("({["):
                brackets.append(c)
            if c in set("]})"):
                if not brackets or brackets.pop() != mirror[c]:
                    return False
        return True if not brackets else False

# https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        left, right, top, bottom = 0, len(matrix) - 1, 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                (
                    matrix[left + i][top], 
                    matrix[right][top + i], 
                    matrix[right - i][bottom], 
                    matrix[left][bottom - i]
                ) = (
                    matrix[right][top + i],
                    matrix[right - i][bottom],
                    matrix[left][bottom - i],
                    matrix[left + i][top]
                )
            left += 1
            top += 1
            bottom -= 1
            right -= 1

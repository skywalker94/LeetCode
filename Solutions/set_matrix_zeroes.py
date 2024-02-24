# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        zero_rows = {}
        zero_columns = {}

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                element = matrix[row][column]
                
                if element == 0:
                    zero_rows[row] = True
                    zero_columns[column] = True
                    
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if column in zero_columns or row in zero_rows:
                        matrix[row][column] = 0
        
        return matrix

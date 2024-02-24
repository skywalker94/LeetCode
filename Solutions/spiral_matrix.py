# https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.visited = {}

    def allowed(self, location):
        return (location not in self.visited and
            0 <= location[0] < self.rows and
            0 <= location[1] < self.columns
        )

    def step(self, location, direction):
        changes = {'r': (0, 1), 'd': (1, 0), 'l': (0, -1), 'u': (-1, 0)}
        change = changes[direction]
        return location[0] + change[0], location[1] + change[1]
    
    def nextLocation(self, location, direction):
        rotation = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
        new_r, new_c = self.step(location, direction)
        if self.allowed((new_r, new_c)):
            return (new_r, new_c), direction
        
        direction = rotation[direction]
        new_r, new_c = self.step(location, direction)
        if self.allowed((new_r, new_c)):
            return (new_r, new_c), direction
        
        return None, direction

    def spiralOrder(self, matrix):
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        if self.rows * self.columns == 1:
            return [matrix[0][0]]

        direction = 'r'
        location = (0, 0)
        seen = []
        while location:
            seen.append(matrix[location[0]][location[1]])
            self.visited[location] = True
            location, direction = self.nextLocation(location, direction)

        return seen

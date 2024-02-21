# https://leetcode.com/problems/clone-graph/

"""
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node, cloned = {}):
        if not node:
            return None
        if node in cloned:
            return cloned[node]

        new = Node(node.val)
        cloned[node] = new

        for n in node.neighbors:
            new.neighbors.append(self.cloneGraph(n, cloned))
        return new

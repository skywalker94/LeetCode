# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def extractValues(self, node, vals = []):
        if node:
            vals.append(node.val)
            self.extractValues(node.next, vals)
        return vals

    def mergeKLists(self, lists):
        values = []
        for ll in lists:
            values += self.extractValues(ll, [])
        if not values or len(values) < 1:
            return None
        values = sorted(values)
        current = ListNode(values[0])
        head = current
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

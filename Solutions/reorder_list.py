# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        nodes, l = [], head
        while l:
            nodes.append(l)
            l = l.next
        left, right = 0, len(nodes) - 1
        current = new_head = ListNode(0)
        while left <= right:
            current.next = nodes[left]
            current = current.next
            if left < right:
                current.next = nodes[right]
                current = current.next
            current.next = None
            left += 1
            right -= 1
        return new_head.next

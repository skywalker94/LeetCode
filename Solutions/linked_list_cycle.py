# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head: return None
        rabbit, turtle = head, head
        while rabbit and turtle:
            if rabbit.next:
                rabbit = rabbit.next.next
            else:
                return False
            turtle = turtle.next
            if rabbit and turtle and rabbit == turtle:
                return True
        return False

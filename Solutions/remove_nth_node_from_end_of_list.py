# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def extractValues(self, linkedlist, values = []):
        if linkedlist:
            values.append(linkedlist.val)
            self.extractValues(linkedlist.next, values)
        return values

    def removeNthFromEnd(self, head, n):
        values = self.extractValues(head, [])
        if len(values) == 1:
            return None
        if len(values) - n == 0:
            return head.next
        count = 0
        current = head
        while current:
            if count == len(values) - n - 1:
                current.next = current.next.next
                break
            count += 1
            current = current.next
        return head

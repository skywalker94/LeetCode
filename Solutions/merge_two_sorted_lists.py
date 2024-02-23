# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def extractValues(self, linkedlist, values = []):
        if linkedlist:
            values.append(linkedlist.val)
            self.extractValues(linkedlist.next, values)
        return values

    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2
        values = []
        for ll in [list1, list2]:
            values += self.extractValues(ll, [])
        values = sorted(values)
        head = ListNode(values[0])
        current = head
        for v in values[1:]:
            current.next = ListNode(v)
            current = current.next
        return head

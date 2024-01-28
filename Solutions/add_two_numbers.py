# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_list_node(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node

class Solution(object):
    def value(self, l):
        if l:
            return l.val
        return 0
    def next(self, l):
        if l:
            if l.next:
                return l.next
        return None
    def update_carry(self, sum):
        if sum > 9:
                return 1
        return 0
    def list_to_linked_list(self, simple_list):
        linked_list = LinkedList()
        for value in reversed(simple_list):
            linked_list.add_list_node(value)
        return linked_list
    
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sums = []
        while True:
            num_1 = self.value(l1)
            num_2 = self.value(l2)
            sum = num_1 + num_2 + carry
            carry = self.update_carry(sum)
            sums.append(sum % 10)
            # print("digit = {0} and carry = {1}".format(sum % 10, carry))
            
            l1 = self.next(l1)
            l2 = self.next(l2)
            
            if not l1 and not l2:
                if carry == 1:
                    sums.append(1)
                break
        return (self.list_to_linked_list(sums)).head

# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def create_list(self, value, head_node):
        head_node.val = value
        return head_node

    def add_to_list(self, value, previous_node):
        current_node = ListNode(value, None)
        previous_node.next = current_node
        return current_node

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head_node = ListNode(-1, None)
        current_node = head_node
        while True:
            num_1 = self.value(l1)
            num_2 = self.value(l2)
            sum = num_1 + num_2 + carry
            
            if current_node.val == -1:
                current_node = self.create_list(sum % 10, head_node)
            else:
                current_node = self.add_to_list(sum % 10, current_node)
            carry = self.update_carry(sum)

            l1 = self.next(l1)
            l2 = self.next(l2)

            if not l1 and not l2:
                if carry == 1:
                    current_node = self.add_to_list(1, current_node)
                break

        return head_node

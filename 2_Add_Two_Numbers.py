# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, solution, traverser = 0, None, None
        while l1 or l2 or carry:
            digit_sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if not solution:
                traverser = solution = ListNode(digit_sum % 10)
            else:
                traverser.next = ListNode(digit_sum % 10)
                traverser = traverser.next
            carry = digit_sum // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b_str = ''
        while head:
            b_str += str(head.val)
            head = head.next
        return int(b_str, 2)
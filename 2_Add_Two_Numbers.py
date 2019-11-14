# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum_list = ListNode(0)
        traverse = sum_list
        slow = None
        while(l1 or l2):
            if l1: # l1 not exhausted
                traverse.val += l1.val
                l1 = l1.next
            if l2: # l2 not exhausted
                traverse.val += l2.val
                l2 = l2.next
            traverse.next = ListNode(traverse.val // 10)
            traverse.val = traverse.val % 10            
            slow = traverse
            traverse = traverse.next
        if traverse.val == 0:
            slow.next = None
        return sum_list
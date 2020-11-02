# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
常规双pointer 思路
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1 
        p2 = l2 
        dummy = ListNode()
        cur = dummy
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next
            else:
                cur.next = p2
                cur = p2
                p2 = p2.next 
        while p1:
            cur.next = p1 
            cur = p1 
            p1 = p1.next
        while p2:
            cur.next = p2 
            cur = p2
            p2 = p2.next 
        return dummy.next

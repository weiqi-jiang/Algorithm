# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
iteratively 方法
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummyhead = None
        p1 = dummyhead
        p2 = head
        
        while p2:
            tmp = p2.next
            p2.next = p1 
            p1 = p2 
            p2 = tmp
        return p1
"""
recursively 
"""

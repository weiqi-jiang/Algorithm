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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:		
        def split(head):
            dummy = ListNode()
            dummy.next = head
            walker, runner = dummy, dummy
            while runner and runner.next:
                walker = walker.next
                runner = runner.next.next
            p1 = dummy.next 
            p2 = walker.next 
            walker.next = None
            return p1, p2
        
        def count_node(head):
            if not head:
                return 0
            counter = 0
            cur = head
            while cur:
                cur = cur.next
                counter += 1
            return counter
        
        def helper(head):
            counter = count_node(head)
            if counter == 0:
                return None 
            if counter == 1:
                return head 
            if counter == 2:
                p1,p2 = head, head.next 
                p2.next = p1 
                p1.next = None 
                return p2
            p1,p2 = split(head)
            p3,p4 = helper(p1), helper(p2)
            res = p4
            while p4 and p4.next:
                p4 = p4.next
            p4.next = p3 
            return res 
        return helper(head)
		
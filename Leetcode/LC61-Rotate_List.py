# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
step
1. 先找到整个list的长度
2. index 为 length-step 就是breakpoint
3. 重新构造list
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        
        length = self.findListLength(head)
        step = k%length
        break_point = length-step
		
        dummyhead = ListNode(None)
        dummyhead.next = head
        cur = dummyhead
        for i in range(break_point):
            cur = cur.next
		
		# p1 is the breaking node ,p2 = p1.next/current p2 is the head node in new rotated list
        p1,p2 = cur,cur.next
        new_head = p2
        if not p2:
            return dummyhead.next
        while p2.next:
            p2 = p2.next
        
        p2.next = head
        p1.next = None
        return new_head
        
        
    def findListLength(self,head):
        count = 1
        cur = head
        
        while cur.next:
            cur = cur.next
            count += 1
        return count
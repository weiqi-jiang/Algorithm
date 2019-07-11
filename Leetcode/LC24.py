# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        p1,p2 = head,head.next
        return self.helper(p1,p2)
  
    
    def helper(self,n1,n2):
        if n2.next and n2.next.next:
		# 如果 这一对node 后面还有一对node的话
            n3 = n2.next
            n4 = n2.next.next
            n2.next = n1
            n1.next = self.helper(n3,n4)
        else:
		# 如果没有一对了 就分情况考虑是只剩一个节点了 还是没有节点了
            if n2.next and not n2.next.next:
                n3 = n2.next
                n2.next = n1
                n1.next = n3
            else:
                n2.next = n1
                n1.next = None
        return n2
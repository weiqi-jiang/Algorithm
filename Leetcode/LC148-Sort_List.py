"""
merge sort的linked list版本
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        return self.sorting(head)
        
    def sorting(self,head):
        if not head:
            return None
        if head and not head.next:
            return head
        left,right = self._split(head)
        h1,h2 = self.sorting(left),self.sorting(right)
        return self._merge(h1,h2)
    
    def _split(self,head):
        if head and not head.next:
            return head
        if not head:
            return None
        p1,p2 = head,head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        res = p1.next
        p1.next = None
        
        return head,res
        
    def _merge(self, p1,p2):
        dummyhead = ListNode(0)
        curnode = dummyhead
        while p1 and p2:
            if p1.val <p2.val:
                curnode.next = p1
                curnode = curnode.next
                p1 = p1.next
            else:
                curnode.next = p2
                curnode = curnode.next
                p2 = p2.next
        while p1:
            curnode.next = p1
            p1 = p1.next
            curnode = curnode.next
        while p2:
            curnode.next = p2
            p2 = p2.next
            curnode = curnode.next
        return dummyhead.next
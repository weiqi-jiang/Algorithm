class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        bp = self._findBreakPoint(head)
        p2 = self._reverseList(bp)
        p1 = head
        self._mergeList(p1,p2)
        return head
        
    def _findBreakPoint(self,head):
        p1,p2 = head,head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        temp = p1.next
        p1.next = None
        return temp
    
    
    
    def _reverseList(self,head):
        pre = None
        while head:
            nextnode = head.next
            head.next = pre
            pre = head
            head = nextnode
        return pre
    
    
    def _mergeList(self,p1,p2):
        while p1 and p2:
            p1next = p1.next
            p1.next = p2
            p1 = p1next
            p2next = p2.next
            p2.next = p1
            p2 = p2next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        return self.remove(head,val)
        
    def remove(self,head,val):
        if not head:
            return 
        dummyhead = ListNode(None)
        dummyhead.next = head
        cur = dummyhead
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyhead.next
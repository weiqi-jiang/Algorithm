class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        p1,p2 = head,head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        else:
            return None   
        p3 = head
        while p3 is not p1:
            p1 = p1.next
            p3 = p3.next
        return p3
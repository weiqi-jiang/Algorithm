
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummyhead = None
        pre,cur = dummyhead,head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre
            
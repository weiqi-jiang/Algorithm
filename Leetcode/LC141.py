class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return False
        walker,runner = head,head.next
        while runner.next and runner.next.next:
            if walker == runner:
                return True
            walker = walker.next
            runner = runner.next.next
        return False
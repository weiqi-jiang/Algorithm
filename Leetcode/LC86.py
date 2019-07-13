class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        dummybefore = ListNode(None)
        dummyafter = ListNode(None)
        before = dummybefore
        after = dummyafter
        
        node=  head
        while node:
            if node.val<x:
                before.next = node
                before = before.next
            else:
                after.next = node
                after = after.next
            node = node.next
        after.next = None
        before.next = dummyafter.next
        
        return dummybefore.next
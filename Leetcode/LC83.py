class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        dummyhead = ListNode(None)
        dummyhead.next = head
        p1,p2 = dummyhead,head
        while p2:
            if p1.val != p2.val:
                p1 = p1.next 
                p2 = p2.next
            else:
                p2 = p2.next
                p1.next = p2
        return dummyhead.next
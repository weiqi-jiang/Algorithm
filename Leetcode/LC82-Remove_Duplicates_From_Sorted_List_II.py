"""
dummy + two pointer
注意一下逻辑即可
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        dummyhead = ListNode(None)
        dummyhead.next = head
        p1,p2 = dummyhead,head
        while p2.next:
            if p2.val != p2.next.val:
            
                p1 = p1.next
                p2 = p2.next
            else:
                while p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                if p2.next:
                    p1.next = p2.next
                    p2 = p2.next
                else:
                    p1.next = None
        return dummyhead.next
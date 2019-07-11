# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummyhead = ListNode(None)
        dummyhead.next = head
        walker, runner = dummyhead,dummyhead
        while n>0:
            runner = runner.next
            n -= 1
        while runner.next:
            runner = runner.next
            walker = walker.next
        walker.next = walker.next.next
        return dummyhead.next
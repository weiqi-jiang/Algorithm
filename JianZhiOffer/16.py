
def reverse_linkedlist4(head):
    if head is None or head.next is None:
        return head
    else:
        newhead=reverse_linkedlist4(head.next)
        head.next.next=head
        head.next=None
    return newhead

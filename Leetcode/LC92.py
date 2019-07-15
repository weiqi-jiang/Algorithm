class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        left,right = head,head
        count = 1
        while count <m:
            left = left.next
            right = right.next
            count+=1
        value = [left.val]
        while count<n:
            right = right.next
            count +=1
            value.append(right.val)
        while value:
            left.val = value[-1]
            value.pop()
            left = left.next
        return head
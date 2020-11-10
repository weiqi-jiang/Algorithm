"""
lc206 的medium版本
加上了M，N区间的限制
这里有取巧的地方，找到N节点的时候把M,N之间的元素值记录下来，M向前找N的时候
就把value倒序
"""

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
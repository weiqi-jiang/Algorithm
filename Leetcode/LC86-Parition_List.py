"""
extra space的思路  相当于把小于 和大于的元素分别放入另外两个list
然后合并这两个list
"""
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
"""
其实还有一种思路，先遍历一遍找到val， sorted 
然后再遍历一遍 把所有元素值改成对应的value就行
"""
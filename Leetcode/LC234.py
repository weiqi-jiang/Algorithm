# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
实现这个功能不难，先遍历一遍 val存数组，然后判断数组是否是回文就行
难点在于O(N) TIME O(1) SPACE
runner walker 的思路 只是在walker往前走的时候，需要把走过的节点reverse，这样停下来的时候 walker 和walker.next 
即为从中间分开的两个linked list的起点，分奇偶去判断是否是回文即可，满足时空要求
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode()
        dummy.next = head
        cur = None
        walker,runner = dummy,dummy
        tmp = walker.next
        while runner and runner.next:
            runner = runner.next.next
            walker = tmp
            tmp = walker.next 
            walker.next = cur 
            cur = walker
        #奇数
        if not runner:
            p1,p2 = walker.next, tmp
        else:
            p1,p2 = walker, tmp 
            
        while p1 and p2:
            if p1.val != p2.val:
                return False 
            p1 = p1.next 
            p2 = p2.next 
        return True 
            
        
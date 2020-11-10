"""
1. 先用runner walker的方法找到第一个汇合点
2. 然后用第三个指针指向头部，汇合点和头部同时走
3. 第二个汇合点就circle起点

原因:
1.设circle前的路径长X, circle 长C， circle起点到第一个汇合点的距离为x
2. 2(L+X) = L+C+X ->  L + X = C  ->  C-X = L
3.我们知道了C-X=L 也就是说第一个汇合点到circle起点的距离是L正好等于头部到circle起点的位置
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        p1,p2 = head,head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        else:
            return None   
        p3 = head
        while p3 is not p1:
            p1 = p1.next
            p3 = p3.next
        return p3
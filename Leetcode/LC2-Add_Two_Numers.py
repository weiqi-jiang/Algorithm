# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
没什么难度，dummynode解法
和merge sort中的merge有点像，注意进位就好了
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        return self.link(l1,l2)
        
        
    def link(self,node1,node2):
        dummyNode = ListNode(None)
        curNode = dummyNode
        forward = 0
        while node1 and node2:
            value = node1.val + node2.val + forward
            if value>=10:
                value -= 10
                forward = 1
            else:
                forward = 0
            tempNode = ListNode(value)
           # print(tempNode.val)
            curNode.next = tempNode
            curNode = tempNode
            node1,node2 = node1.next,node2.next
            
            
        if node1:
            node = node1 
        else: 
            node = node2
        while node:
            value = node.val + forward
            if value>=10:
                value -= 10
                forward = 1
            else:
                forward = 0
            tempNode = ListNode(value)
            curNode.next = tempNode
            curNode = tempNode
            node = node.next
        if forward == 1:
            curNode.next = ListNode(1)
        return dummyNode.next
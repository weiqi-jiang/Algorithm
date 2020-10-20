# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
思路： 有点讨巧，因为我们不能访问到head of linked list,所以不能从头访问
其实删除一个节点而且题目中说了，不是尾节点，那么就可以把后面node的值赋值到当前node，然后删除后一个节点，变相达到了删除的目的。
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        next_next_node = next_node.next
        
        node.val = next_node.val
        node.next = next_next_node
        
        
        
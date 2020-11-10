"""
LC108的变种，把sorted array 改成了sort list
新增了一个找到mid的难度
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        return self.build(head)
        
    def build(self,head):
        root,left,right = self.findmid(head)
        if not root:
            return None
        treeroot = TreeNode(root.val)
        treeroot.left = self.build(left)
        treeroot.right = self.build(right)
        return treeroot
    
    def findmid(self,head):
        if not head:
            return None,None,None
        if head and not head.next:
            return head,None,None
        walker,runner = head,head.next
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
        leftnode  = head
        rightnode = walker.next.next
        root = walker.next
        walker.next = None
        return root,leftnode,rightnode
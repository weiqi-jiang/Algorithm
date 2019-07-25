class Solution:
    def GetNext(self, pNode):
        # write code here
        
        if pNode.right:
            return self._inorder(pNode.right)
        else:
            return self._findfather(pNode)
        
        
        
    def _findfather(self,root):
        if not root.next:
            return None
        else:
            father = root.next
            if father.left == root:
                return father
            else:
                return self._findfather(root.next)
        
        
    def _inorder(self,root):
        if not root.left and not root.right:
            return root
        if root.left:
            return self._inorder(root.left)
        return root
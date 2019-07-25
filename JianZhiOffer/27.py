# 解法一
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return  
        return self.convertToList(pRootOfTree)
       
        
    def convertToList(self,root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        left = self.convertToList(root.left)
        if left:
            cur = left
            while cur.right:
                cur = cur.right
            root.left = cur
            cur.right = root
        right = self.convertToList(root.right)
        if right:
            right.left = root
            root.right = right
        if left:
            return  left
        else:
            return root
# 改进版
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return  
        left,right = self.convertToList(pRootOfTree)
        return left
        
    def convertToList(self,root):
        if not root:
            return None,None
        if not root.left and not root.right:
            return root,root
        
        leftfirst,leftlast = self.convertToList(root.left)
        rightfirst,rightlast = self.convertToList(root.right)
            
        if leftfirst and leftlast:
            root.left = leftlast
            leftlast.right = root
			
			
        if rightfirst and rightlast:
            root.right = rightfirst
            rightfirst.left = root
			
			
        if leftfirst and leftlast:
            if rightfirst and rightlast:
                return leftfirst,rightlast
            else:
                return leftfirst,root
        else:
            if rightfirst and rightlast:
                return root,rightlast
            else:
                return root,root
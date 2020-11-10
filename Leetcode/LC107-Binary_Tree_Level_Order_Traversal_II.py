"""
很没有诚意的题目，无非是level order traversal 然后倒序一下
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while True:
            nextlevel,cur  = [],[]
            while stack:
                node = stack.pop(0)
                cur.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            res.append(cur)
            stack = nextlevel
            if not stack:
                break
        
        return res[::-1]
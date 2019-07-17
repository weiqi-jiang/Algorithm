class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res  =[]
        self.helper([root],res)
        return res
        
        
    def helper(self,Level,res):
        while Level:
            level = Level
            nextLevel = []
            cur = []
            while level:
                node = level.pop(0)
                cur.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            Level = nextLevel
            res.append(cur)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        self.helper([root],res)
        return res
        
        
        
    def helper(self,Level,res):
        flag = 1
        
        while Level:
            level = Level
            cur, nextlevel = [], []
            while level:
                node = level.pop()
                cur.append(node.val)
                if flag ==1:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                if flag == -1:
                    if node.right:
                        nextlevel.append(node.right)
                    if node.left:
                        nextlevel.append(node.left)
            flag = -flag
            Level = nextlevel
            res.append(cur)
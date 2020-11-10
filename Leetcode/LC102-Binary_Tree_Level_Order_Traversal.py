"""
双while loop
内部while loop是遍历同一level，外部用于控制整个流程
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
 
        if not root:
            return []
        res  =[]
        self.helper([root],res)
        return res
  
"""
不想用双while loop的话 就需要记录当前的level，如果level变化了，新建val list
"""  
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_level = 0
        queue = [(root,1)]
        result = []
        while queue:
            node, level = queue.pop(0)
            if level > cur_level:
                result.append([node.val])
                cur_level += 1
            else:
                result[-1].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return result     

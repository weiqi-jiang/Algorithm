"""
双栈法
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack1 = [root]
        stack2 = []
        res = []
        if not root:
            return []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while len(stack2) > 0:
            res.append(stack2.pop().val)
            
        return res
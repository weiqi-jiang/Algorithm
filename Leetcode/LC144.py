class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                ret.append(node.val)
                stack.append(node.left)
        return ret
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res,s = [],[]
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return res
            node = s.pop()
            res.append(node.val)
            root = node.right
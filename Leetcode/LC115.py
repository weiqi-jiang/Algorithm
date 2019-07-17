class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.dfs(root)
    def dfs(self,root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                self.dfs(root.left)
                self.dfs(root.right)
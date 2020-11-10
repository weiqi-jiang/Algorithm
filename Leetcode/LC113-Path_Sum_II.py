"""
LC112的变种，LC112 逻辑判断，存在返回true即可，不需要找到所有，该题需要找到所有路径
需要保存当前路径
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        
        def helper(root, cur_path,cur_sum, paths, target):
            if not root:
                return 
            if not root.left and not root.right:
                if cur_sum+root.val == target:
                    paths.append(cur_path+[root.val])
                    return a
            helper(root.left, cur_path+[root.val], cur_sum+root.val, paths, target)
            helper(root.right, cur_path+[root.val], cur_sum+root.val, paths, target)
        
        helper(root,[],0,paths,sum)
        return paths
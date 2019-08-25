tree = [1,2,3,4,-1,-1,-1]
tree = [None] + tree
def dfs(tree,res,i):
    if i>=len(tree) or tree[i] == -1:
        return 0
    left = dfs(tree,res,i*2)
    right = dfs(tree,res,i*2+1)
    res.append(left + right)
    return max(left+1,right+1)
res = []
dfs(tree,res,1)
print(max(res))
'''
二维M*N 矩阵，matrix[i][j] 如果为负 说明 玩家需要战斗，减去-matrix[i][j] , 如果是正，是补给品，加上matrix[i][j]血量，全程血量不能小于1
玩家从0,0 开始到右下角，只能往右或者往下，返回玩家初始血量最小是多少才可能到达右下角
例子 
-2  -3   3
-5  -10  1
0   30  -5
return 7 路径是 -2 -3 3 1 -5

'''

m,n = 3,3
nums = [-2, -3, 3, -5, -10, 1, 0, 30, -5]
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(nums[i*n+j])
    matrix.append(row)
res = []

def solution(res,matrix,i,j,count,path):
    cur = matrix[i][j] + count
    p = path + [cur]
    if i < m-1:
        solution(res,matrix,i+1,j,cur,p)
    if j<n-1:
        solution(res,matrix,i,j+1,cur,p)
    if i==m-1 and j==n-1:
        res.append(p)
        return 
solution(res,matrix,0,0,0,[])
res = [min(r) for r in res]
r = max(res)
if r >=1:
    print(0)
else:
    print(-r+1)
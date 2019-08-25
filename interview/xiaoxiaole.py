

from copy import deepcopy

def _float(matrix,i,j):
	'''
	'x'上浮
	'''
    while i>=1:
        matrix[i][j],matrix[i-1][j] = matrix[i-1][j],matrix[i][j]
        i-=1
def sink(matrix):
	'''
	输入： 把某一组相连的元素设为‘x’之后的matrix
	输出： 把‘x’ 上浮  变相实现有效元素下沉 模拟重力机制
	'''
    for col in range(5):
        for row in range(5):
            if matrix[row][col] == 'x':
                _float(matrix,row,col)
    return matrix

def findgroup(matrix):
	'''
	找出matrix中有几组可以消除的group, group中包含一个group所有元素的index
	return list[group]
	'''
    groups = []
    v = [[0 for i in range(5)] for j in range(5)]
    for i in range(5):
        for j in range(5):
            if not v[i][j] and matrix[i][j] != 'x':
                s = [(i,j)]
                target = matrix[i][j]
                g = []
                while s:
                    cur = s.pop()
                    g.append(cur)
                    m,n = cur[0],cur[1]
                    v[m][n] = 1
                    if m > 0 and matrix[m-1][n] == target and not v[m-1][n]:
                        s.append((m-1,n))
                    if m<4 and matrix[m+1][n] == target and not v[m+1][n]:
                        s.append((m+1,n))
                    if n > 0 and matrix[m][n-1] == target and not v[m][n-1]:
                        s.append((m,n-1))
                    if n< 4 and matrix[m][n+1] == target and not v[m][n+1]:
                        s.append((m,n+1))
                else:
                    groups.append(g)
    groups = [g for g in groups if len(g)>=3]
    return groups
                            
def clear(matrix,g):
	'''
	把group 中所有对应的index 设为'x'
	'''
    for index in g:
        i,j = index[0],index[1]
        matrix[i][j] = 'x'
    return matrix


def out(matrix):
	'''
	数matrix 剩下几个非'x'的元素
	'''
    count = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j]!= 'x':
                count += 1
    return count
    
    
def solution(matrix,res):
	# 找到 所有可以消除的group
    groups = findgroup(matrix)
	# 如果没有把当前matrix 非’x‘元素个数放入res
    if not groups:
        res.append(out(matrix))
        return 
	# 对于每一个可以消除的group
    for g in groups:
		# 首先要创建副本，不然效果混淆
        temp = deepcopy(matrix)
		# group中元素设为'x'
        cur_mat = clear(temp,g)
        cur_mat2 = deepcopy(cur_mat)
		# 把 ’x‘元素上浮，实现重力效果，然后把实现重力效果之后的新矩阵当做参数进行递归
        solution(sink(cur_mat2),res)


if __name__ == '__main__':  
	matrix = [
	[3, 1, 2, 1, 1],
	[1, 1, 1, 1, 3],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[3, 1, 2, 2, 2]
	]    
	res = []
	m = deepcopy(matrix)
	solution(m,res)
	#res 中最小值就是结果
	print(min(res))
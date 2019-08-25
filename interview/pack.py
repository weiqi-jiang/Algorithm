def zeroOnePack(H,N,values,weights,dim=2, is_exact=False):
	'''
	 0 1背包问题，一个物品只有一个
	params:
	N :物品数
	H :背包重量 
	values : 物品价格
	weights :物品重量
	dim :表示动态规划的维度 	支持 1 or 2
	is_exact: 是否要求必须装满背包
	'''
	values = [0]+ values
	weights = [0]+ weights
	
	if dim == 2:
		# init
		if not is_exact:
			matrix = [[0 for i in range(H+1)]for j in range(N+1)]
		else:
			matrix = [[-float('INF') for i in range(H+1)] for j in range(N+1)]
			for r in range(len(matrix)):
				matrix[r][0] = 0
		# dp
		for i in range(1,N+1):
			for v in range(1,H+1):
				if weights[i] <= v:
					matrix[i][v] = max(matrix[i-1][v],matrix[i-1][v-weights[i]] + values[i])
				else:
					matrix[i][v] = matrix[i-1][v]
		return matrix[-1][-1]
		
	elif dim == 1:
		# init 
		if not is_exact:
			stat = [0 for i in range(H+1)]
		else:
			stat = [-float('INF') for i in range(H+1)]
			stat[0] = 0
		# dp
		for i in range(1,N+1):
			for v in range(H,0,-1):
				if weights[i] <= v:
					stat[v] = max(stat[v],stat[v-weights[i]]+values[i])
		return stat[-1]
				
	else:
		return 'Dimension 仅支持1 或 2'


def completePack(H,V,values,weights,dim = 2,is_exact = False):
	'''
	 完全背包问题，一个物品可以拿无限次
	params:
	N :物品数
	H :背包重量 
	values : 物品价格
	weights :物品重量
	dim :表示动态规划的维度 	支持 1 or 2
	is_exact: 是否要求必须装满背包
	'''
	values = [0]+ values
	weights = [0]+ weights
	
	if dim == 2:
		# init 
		if not is_exact:
			matrix = [[0 for i in range(H+1)]for j in range(N+1)]
		else:
			matrix = [[-float('INF') for i in range(H+1)] for j in range(N+1)]
			for r in range(len(matrix)):
				matrix[r][0] = 0
		# dp		
		for i in range(1,N+1):
			for v in range(1,H+1):
				for k in range(v//weights[i]+1):
					matrix[i][v] = max(matrix[i][v],matrix[i-1][v-k*weights[i]] + k*values[i])
		return matrix[-1][-1]
		
	elif dim == 1:
		#init 
		if not is_exact:
			stat = [0 for i in range(H+1)]
		else:
			stat = [-float('INF') for i in range(H+1)]
			stat[0] = 0
		# dp
		for i in range(1,N+1):
			for v in range(H,0,-1):
				for k in range(v//weights[i]+1):
					stat[v] = max(stat[v],stat[v-k*weights[i]] + k*values[i])
		return stat[-1]
				
	else:
		return 'Dimension 仅支持1 或 2'


if __name__ == '__main__':
	N= 5
	H = 15
	values = [12,3,10,3,6]
	weights = [5,4,7,2,6]
	dim = 2
	print('01背包问题： ', zeroOnePack(H,N,values,weights,dim,True))
	print('完全背包问题： ', completePack(H,N,values,weights,dim,True))
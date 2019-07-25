class solution1:
	
	def nDicePoints(self,n,p):
		if n<1:
			return 0
		if p<n or p>6*n:
			return 0
		if n ==1:
			return 1
		res  = 0
		for i in range(1,7):
			res += self.nDicePoints(n-1,p-i)
		return res
		
	def diceProbability(self,n):
		ntotal = 6**n
		res  =[]
		for i in range(n,6*n+1):
			res.append(self.nDicePoints(n,i))
		print(res)
	
class solution2:
	
	def generatePointTable(self,n):
		mapset = []
		map1 = {i:1 for i in range(1,7)}
		mapset.append(map1)
		for i in range(2,n+1):
			nextmap = {}
			for j in range(i,i*6+1):
				nextmap[j] =0
				for m in range(1,7):
					if mapset[i-2].get(j-m):
						
						nextmap[j] += mapset[i-2][j-m]
			mapset.append(nextmap)
		return mapset[-1]

s = solution1()
s.diceProbability(3)

s2 = solution2()
print(s2.generatePointTable(6))
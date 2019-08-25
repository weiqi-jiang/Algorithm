class solution():

	def getNsum(self,n,flag):
		
		res = (n>0) and (flag += self.getNsum(n-1,flag))
		return flag

s = solution()
print(s.getNsum(10,0))
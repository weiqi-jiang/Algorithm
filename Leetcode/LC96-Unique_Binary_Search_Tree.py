"""
这其实不是一个树相关的题目，而是DP题
要想清楚这个状态转移方程是很难的
"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        g = [1]*(n+1)
        g[0]=g[1]=1
        for i in range(2,n+1):
            temp = 0
            for j in range(1,i+1):
                temp += g[j-1]*g[i-j]
            g[i] = temp
        return g[n]
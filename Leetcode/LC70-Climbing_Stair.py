"""
最基本的动态规划问题， 但是注意不要写成递归了


def helper(n):
    if n == 1:
        return 1
    if n==2:
        return 2
    return helper(n-1) + helper(n-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        tmp = [0]*n
        tmp[0] = 1
        tmp[1] = 2
        
        for i in range(2, n):
            tmp[i] = tmp[i-1] + tmp[i-2]
        return tmp[-1]
        
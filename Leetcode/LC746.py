class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost)==1 or len(cost) == 2:
            return min(cost)
        stat = cost + [0]
        
        for i in range(2,len(stat)):
            stat[i] += min(stat[i-1],stat[i-2])
        return stat[-1]
"""
这个动态规划的思路不太好想,参考的discuss里面别人的解法
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        
        temp = [gas[i] - cost[i]  for i in range(len(gas))]
        if sum(temp)<0:
            return -1
        
        startindex = 0
        gas_remain = 0
        for i in range(len(temp)):
            gas_remain += temp[i]
            if gas_remain <0:
                gas_remain = 0 
                startindex= i+1
            
        return startindex
"""
常规思路，很明了
为了方便，不同的起点就把gas和cost按照起点重新旋转一下
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def helper(gas, cost):
            r = 0
            for i in range(len(gas)):
                r+= gas[i] -cost[i]
                if r<0:
                    return False
            return True

                
        for pivot in range(len(gas)):
            gas_ = gas[pivot:] + gas[:pivot]
            cost_ = cost[pivot:] + cost[:pivot]
            if helper(gas_,cost_):
                return pivot 
        return -1
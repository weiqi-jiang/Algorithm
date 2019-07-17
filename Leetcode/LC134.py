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
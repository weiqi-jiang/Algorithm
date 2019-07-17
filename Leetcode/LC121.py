class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)<2:
            return 0
        temp1 = [0]
        for i in range(1,len(prices)):
            temp1.append(prices[i]-prices[i-1])
        for i in range(1,len(prices)):
            if temp1[i-1]>=0:
                temp1[i] += temp1[i-1]
        return max(temp1)
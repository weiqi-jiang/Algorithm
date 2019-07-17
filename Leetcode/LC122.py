class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy,sell,profit = prices[0],prices[0],0
        for i in range(1,len(prices)):
            if prices[i]>sell:
                sell = prices[i]
            else:
                profit+=sell-buy
                buy,sell = prices[i],prices[i]
        profit += sell -buy
        return profit
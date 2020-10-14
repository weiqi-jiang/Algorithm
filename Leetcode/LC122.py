"""
思路一： Two Pointer， 分别代表买和卖，如果未来价格下跌，买卖同时更新为最新价格，否则只有卖指针更新，只需要注意遍历完时最后需要更新一次profit
"""
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
		
"""
思路二： Two Pointer, 更确切的说是双while循环，先一直往价格低的方向走，局部最低点时，buy指针固定，然后sell指针一直往上走，走到头，sell-buy,然后循环两个while，
也就是说一共有三个while循环。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)== 1:
            return 0
        i,j, profit = 0, 0, 0
        while j<len(prices)-1:
            while j<len(prices)-1 and prices[j]>= prices[j+1]:
                j+=1
            i=j 
            while j<len(prices)-1 and prices[j]<prices[j+1]:
                j+=1
            profit += prices[j]-prices[i]
            
        return profit
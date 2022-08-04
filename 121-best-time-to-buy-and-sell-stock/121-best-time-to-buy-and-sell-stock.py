class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        profit=0
        for ele in prices:
            if(ele<min_price):
                min_price=ele
            if(ele-min_price>profit):
                profit=ele-min_price
        return profit
        
        
#        
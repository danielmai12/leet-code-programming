"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buying_price = prices[0]
        
        # This approach solve the problem: [2, 10, 1, 8, 5, 6, 7] -> max_profit = 8 (buy: 2, sell: 10) instead choose the min_price = 1 and sell after that at 8.
        # It maintains the max_profit while also keeping up with the min_price
        
        for i in range(1, len(prices)):
            profit = prices[i] - buying_price
            
            if profit > max_profit:
                max_profit = profit
                
            if buying_price > prices[i]:
                buying_price = prices[i]
        
        return max_profit
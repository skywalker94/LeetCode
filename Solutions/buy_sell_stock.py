# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy_pos = 0
        for sell_pos in range(1, len(prices)):
            profit = prices[sell_pos] - prices[buy_pos]
            if prices[buy_pos] < prices[sell_pos]:
                max_profit = max(max_profit, profit)
            else:
                buy_pos = sell_pos            
        return max_profit

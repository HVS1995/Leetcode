class Solution:
    def __init__(self):
        self.t = [[-1, -1] for _ in range(5001)]
        
    def maxP(self, prices, day, n, buy):
        if day >= n:
            return 0

        if self.t[day][buy] != -1:
            return self.t[day][buy]

        profit = 0
        if buy:
            consider = self.maxP(prices, day+1, n, False) - prices[day]
            not_consider = self.maxP(prices, day+1, n, True)
            profit = max(profit, consider, not_consider)
        else:
            consider = self.maxP(prices, day+2, n, True) + prices[day]
            not_consider = self.maxP(prices, day+1, n, False)
            profit = max(profit, consider, not_consider)

        self.t[day][buy] = profit
        return profit

    def maxProfit(self, prices):
        n = len(prices)
        return self.maxP(prices, 0, n, True)

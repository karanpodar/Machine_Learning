'''
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # a,b = 0,1
        # profit = 0
        # while a < len(prices):           
        #     if b < len(prices):
        #         if prices[b] - prices[a] > profit:
        #             profit =  prices[b] - prices[a]
        #         b += 1
        #     else:
        #         a += 1
        #         b = a + 1
        # return profit
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
    
sol = Solution()
prices = [7,3,5,1,5,3,6]
print(sol.maxProfit(prices))
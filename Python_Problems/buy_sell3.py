'''
Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # The variables are long for better understanding
        
        # Initialize variables to track minimum prices and maximum profits
        min_price_after_first_buy = float('inf')
        max_profit_after_first_sell = 0
        min_price_after_second_buy = float('inf')
        max_profit_after_second_sell = 0
        
        for price in prices:
            # Update the minimum price for the first buy
            min_price_after_first_buy = min(min_price_after_first_buy, price)
            
            # Calculate profit after the first sell
            max_profit_after_first_sell = max(max_profit_after_first_sell, price - min_price_after_first_buy)
            
            # Update the minimum price for the second buy
            min_price_after_second_buy = min(min_price_after_second_buy, price - max_profit_after_first_sell)
            
            # Calculate profit after the second sell
            max_profit_after_second_sell = max(max_profit_after_second_sell, price - min_price_after_second_buy)
        
        return max_profit_after_second_sell
    

sol = Solution()
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))
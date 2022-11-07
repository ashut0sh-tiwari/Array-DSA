"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

prices = [7,1,5,3,6,4]

def maxProfit(prices):
        buy,sell = 0, 1 #initialising the variables
        maxProfit = 0 #initialising the variables
        while sell< len(prices): #looping till the len of prices
            if prices[buy] < prices[sell]: #if the value of buy is less than sell
                profit = prices[sell] - prices[buy] #calculating the total profit
                maxProfit = max(maxProfit, profit) #updating the variable and using the max value of the variable in each iterations
            else:
                buy = sell #updating the buy variable if its value becomes greater than sell
            sell += 1 #incrementing sell value by one with each iterables

        return maxProfit #returning maxprofit

solution = maxProfit(prices)
print(solution)
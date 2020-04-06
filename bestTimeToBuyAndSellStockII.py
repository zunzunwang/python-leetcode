from typing import List

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

转化为寻找所有的单调递增区间

转化为所有的相邻的增量的累计
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result

    def maxProfit1(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        head = 1
        end = 0
        result = 0

        while head < len(prices):
            if prices[head] >= prices[end]:
                while head < len(prices):
                    if prices[head] >= prices[head - 1]:
                        head += 1
                    else:
                        result += prices[head - 1] - prices[end]
                        end = head
                        head += 1
                        break
                result += prices[head - 1] - prices[end]
            else:
                end = head
                head += 1
        return result

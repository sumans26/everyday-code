# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        # min_left_array = [None]*length
        max_right_array = [None]*length

        min_left = 100000
        max_right = -1

        # for i in range(length):
        #     min_left = min(min_left, prices[i])
        #     min_left_array[i] = (min_left)

        for i in reversed(prices):
            max_right = max(max_right, prices[-1-i])
            max_right_array[-1-i] = (max_right)

        # print("min array", min_left_array)
        print("max array", max_right_array)

        max_profit = 0
        for i in range(length):
            min_left = min(min_left, prices[i])
            if (max_right_array[i] - min_left > max_profit):
                max_profit = max_right_array[i] - min_left
        return max_profit

    def maxProfit(self, prices):
        buy_index = 0
        buy_index_price = prices[buy_index]
        current_sell_index = 1

        max_profit = 0

        while current_sell_index < len(prices):
            if(buy_index_price > prices[current_sell_index]):
                buy_index = current_sell_index
                buy_index_price = prices[current_sell_index]

            current_profit  = prices[current_sell_index] - buy_index_price

            if(current_profit > max_profit):
                max_profit = current_profit
            
            current_sell_index = current_sell_index + 1
        
        return max_profit
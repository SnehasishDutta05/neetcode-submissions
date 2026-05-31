class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        if(len(prices) == 1 or  len(prices) == 0):
            return 0
        if(len(prices) == 2):
            if(prices[1] - prices[0] > max_profit):
                    max_profit = prices[1] - prices[0]
                    # return max_profit

        for i in range(len(prices) - 1):
            j = len(prices) - 1 
            while(j>i):
                if(prices[j] - prices[i] > max_profit):
                    max_profit = prices[j] - prices[i]
                j -= 1 
            
        return max_profit

        
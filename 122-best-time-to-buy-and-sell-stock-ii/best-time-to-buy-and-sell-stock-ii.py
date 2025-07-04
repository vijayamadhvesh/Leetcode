class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_sell = 0
        prev_buy = prices[0]
        profit = 0

        for num in prices[1:]:

            # min_buy = min(min_buy, num)
            # max_sell = max(max_sell, num)

            if num > prev_buy:
                profit += num - prev_buy

            prev_buy = num

        return profit
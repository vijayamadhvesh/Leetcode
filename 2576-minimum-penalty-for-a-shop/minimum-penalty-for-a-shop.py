class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        profit, max_profit  = 0, 0
        best_time = -1

        for i, visit in enumerate(customers):
            if visit == 'Y':
                profit += 1
            else:
                profit -= 1
            
            if profit > max_profit:
                max_profit = profit
                best_time = i
        
        return best_time + 1 # as it is best to close shop after the best profitable day
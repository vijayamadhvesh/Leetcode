class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if "Y" not in customers:
            return 0
        if "N" not in customers:
            return len(customers)
        
        profit = 0
        maxP = 0
        bestCT = 0

        for i,v in enumerate(customers):
            profit += 1 if v == "Y" else -1

            if profit > maxP:
                maxP = profit
                bestCT = i + 1
        return bestCT
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        res = 0
        n = len(customers)
        for arrival, finish in customers:
            if total < arrival:
                total = arrival
            total += finish
            res += (total - arrival)
        return res/n

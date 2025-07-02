class Solution:
    def bestClosingTime(self, customers: str) -> int:
        left_penalty = 0
        right_penalty = customers.count('Y')

        n = len(customers)
        min_penalty = n
        best_time = n

        for i in range(n+1):
            if left_penalty + right_penalty < min_penalty:
                min_penalty = left_penalty + right_penalty
                best_time = i
            if i<n and customers[i] == 'N':
                left_penalty += 1
            if i<n and customers[i] == 'Y':
                right_penalty -= 1
        return best_time

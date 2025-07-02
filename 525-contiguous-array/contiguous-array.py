class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_to_index = {0: -1}
        max_len = 0
        running_sum = 0

        for i, num in enumerate(nums):
            if num == 0:
                running_sum -= 1
            else:
                running_sum += 1

            if running_sum in sum_to_index:
                max_len = max(max_len, i - sum_to_index[running_sum])
            else:
                sum_to_index[running_sum] = i

        return max_len
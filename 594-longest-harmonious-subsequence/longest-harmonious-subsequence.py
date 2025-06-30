class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_length = 0

        unique_list = sorted(counter)

        for i in range(1, len(unique_list)):
            if unique_list[i] - unique_list[i-1] == 1:
                max_length = max(max_length, counter[unique_list[i]] + counter[unique_list[i-1]])
        return max_length
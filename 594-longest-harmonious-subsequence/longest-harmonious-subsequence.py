class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_length = 0
        visit = set()
        for num in nums:
            if num-1 in counter and num not in visit:
                max_length = max(max_length, counter[num] + counter[num-1])
        return max_length
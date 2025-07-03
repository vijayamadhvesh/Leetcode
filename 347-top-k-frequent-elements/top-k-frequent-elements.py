class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        return sorted(counter, key = lambda x: -counter[x])[:k]
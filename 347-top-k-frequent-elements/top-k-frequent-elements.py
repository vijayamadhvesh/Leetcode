class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        freq = []

        for i in range(max(counter.values())+1):
            freq.append([])

        for key, value in counter.items():
            freq[value].append(key)
            
        res = []
        for nums in freq[::-1]:
            if nums:
                res.extend(nums)
        return res[:k]
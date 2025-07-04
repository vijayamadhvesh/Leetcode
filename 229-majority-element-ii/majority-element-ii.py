class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        n_by_3 = len(nums)//3

        for key, value in counter.items():
            if value > n_by_3:
                res.append(key)
        return res
        
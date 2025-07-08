class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = defaultdict(list)

        res = []

        for num in nums:
            value = ''
            for ch in str(num):
                value += str(mapping[int(ch)])
            value = int(value)
            d[value].append(num)
            
        for sorted_key in dict(sorted(d.items())):
            res.extend(d[sorted_key])
        return res
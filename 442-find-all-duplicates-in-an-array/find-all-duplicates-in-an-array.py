class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s, res = set(), set()
        
        for num in nums:
            if num in s:
                res.add(num)
            else:
                s.add(num)
        return list(res)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = [0] * (len(nums)+1)
        res = set()
        for i, num in enumerate(nums):
            if s[num] == 1:
                res.add(nums[i])
            else:
                s[num] = 1
        return list(res)
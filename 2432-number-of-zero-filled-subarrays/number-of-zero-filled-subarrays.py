class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * (n)
        
        if nums[0] == 0:
            res[0] = 1
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                res[i] += 1

                if nums[i-1] == 0:
                    res[i] += res[i-1]
        return sum(res)
            
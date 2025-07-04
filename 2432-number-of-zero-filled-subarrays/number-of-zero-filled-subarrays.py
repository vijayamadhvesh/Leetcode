class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        
        temp = 0
        res = 0

        for n in nums:

            if not n:
                temp += 1
                res += temp
            
            else:
                temp = 0
        
        return res
            
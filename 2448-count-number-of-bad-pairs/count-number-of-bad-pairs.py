class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good = 0
        dict_val = {}
        for j in range(len(nums)):
            key = nums[j] - j
            if key in dict_val:
                good += dict_val[key]
                dict_val[key] += 1
            else:
                dict_val[key] = 1
        
        n = len(nums)
        total = n * (n-1) // 2
        return total - good
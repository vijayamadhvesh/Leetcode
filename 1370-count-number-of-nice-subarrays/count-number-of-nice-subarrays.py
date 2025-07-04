class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {0:1}

        odd_cnt = 0
        res = 0
        for num in nums:
            if num % 2:
                odd_cnt += 1
            
            if odd_cnt - k in d:
                res += d[odd_cnt-k]
            
            if odd_cnt in d:
                d[odd_cnt] += 1
            else:
                d[odd_cnt] = 1
        return res
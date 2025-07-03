class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        rem = {0:1}

        prefix, mod = 0, 0
        for num in nums:
            prefix += num

            mod = prefix%k

            if mod < 0:
                res += k

            if mod in rem:
                res += rem[mod]
                rem[mod] += 1
            else:
                rem[mod] = 1
        return res


        
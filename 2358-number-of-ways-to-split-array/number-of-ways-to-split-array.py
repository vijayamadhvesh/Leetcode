class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*(n+1)
        # prefix_sum[0] = nums[0]

        for i in range(n):
            prefix_sum[i+1] += prefix_sum[i] + nums[i]


        # for i in range(1, n+1):
        i = 0
        res = 0
        while i < n-1:
            if (prefix_sum[i+1] >= prefix_sum[n] - prefix_sum[i+1]):
                res += 1                
            i += 1

        return res       
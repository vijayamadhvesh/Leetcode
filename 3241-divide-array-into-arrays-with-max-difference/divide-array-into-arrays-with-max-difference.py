class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums.sort()

        for i in range(0, n, 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if c-a>k:
                return []
            else:
                res.append([a, b, c])
        return res
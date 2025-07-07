class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0

        for count in counter.values():
            if count == 1:
                return -1

            # Minimum number of operations using 3s and 2s
            # Try to use as many 3s as possible
            ops = count // 3
            if count % 3 == 0:
                res += ops
            else:
                # Use (count // 3 - 1) 3s and two 2s if remainder is 1
                res += ops + 1

        return res
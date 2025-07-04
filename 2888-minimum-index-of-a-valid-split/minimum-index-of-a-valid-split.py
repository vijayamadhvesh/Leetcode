class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dom, freq = max(count.items(), key=lambda x: x[1])
        n = len(nums)
        
        left_count = 0
        for i in range(n - 1):  
            if nums[i] == dom:
                left_count += 1
            
            
            if left_count * 2 > (i + 1) and (freq - left_count) * 2 > (n - i - 1):
                return i
        
        return -1
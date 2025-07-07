class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total = sum(nums)
        heap = [-num for num in nums]
        heapq.heapify(heap)

        while len(heap) > 2:
            largest = -heapq.heappop(heap)
            total -= largest
            if largest < total:
                return total + largest

        return -1
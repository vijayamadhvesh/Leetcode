class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_top = grid[0].copy()
        prefix_bottom = grid[1].copy()

        for i in range(1, n):
            prefix_top[i] += prefix_top[i-1]
            prefix_bottom[i] += prefix_bottom[i-1]

        print(prefix_top)
        print(prefix_bottom)
        res = float('inf')

        for i in range(n):
            top_after = prefix_top[-1] - prefix_top[i]  # grid[0][i+1:]
            bottom_before = prefix_bottom[i-1] if i>0 else 0             # grid[1][:i]
            
            res = min(res, max(top_after, bottom_before))

        return res
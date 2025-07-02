class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_top = [0] * (n + 1)
        prefix_bottom = [0] * (n + 1)

        for i in range(n):
            prefix_top[i+1] = prefix_top[i] + grid[0][i]
            prefix_bottom[i+1] = prefix_bottom[i] + grid[1][i]

        res = float('inf')

        for i in range(n):
            top_after = prefix_top[n] - prefix_top[i+1]  # grid[0][i+1:]
            bottom_before = prefix_bottom[i]             # grid[1][:i]
            res = min(res, max(top_after, bottom_before))

        return res

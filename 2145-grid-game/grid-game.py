class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = 0
        ts = sum(grid[0][1::])
        v = 0
        ans = ts
        for i in range(len(grid[0])-1):
            v += grid[1][i]
            ts -= grid[0][i+1]
            ans = min(ans, max(v, ts))
        return ans
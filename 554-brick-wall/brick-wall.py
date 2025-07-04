class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        d= defaultdict(int)

        
        for row in wall:
            psum = 0
            for i in range(len(row)-1):
                psum += row[i]
                d[psum] += 1
            if psum == 0:
                d[0] = 0

        return len(wall) - max(d.values())
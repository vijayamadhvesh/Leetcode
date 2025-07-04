class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        lseq = max(wall, key=len)
        if len(lseq) == 1:
            return len(wall)

        walls = Counter()

        for bricks in wall:
            total = 0

            for brick in bricks[:-1]:
                total += brick
                walls[total] +=1

        return len(wall) - max(walls.values())
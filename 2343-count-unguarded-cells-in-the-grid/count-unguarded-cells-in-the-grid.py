from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [['a' for _ in range(n)] for _ in range(m)]

        # Mark walls
        for r, c in walls:
            cells[r][c] = 'w'

        # Mark guards
        for r, c in guards:
            cells[r][c] = 'G'

        # Guard directions
        for gr, gc in guards:
            # Left
            for i in range(gc - 1, -1, -1):
                if cells[gr][i] in ('w', 'G'):
                    break
                if cells[gr][i] == 'a':
                    cells[gr][i] = 'g'
            # Right
            for i in range(gc + 1, n):
                if cells[gr][i] in ('w', 'G'):
                    break
                if cells[gr][i] == 'a':
                    cells[gr][i] = 'g'
            # Up
            for i in range(gr - 1, -1, -1):
                if cells[i][gc] in ('w', 'G'):
                    break
                if cells[i][gc] == 'a':
                    cells[i][gc] = 'g'
            # Down
            for i in range(gr + 1, m):
                if cells[i][gc] in ('w', 'G'):
                    break
                if cells[i][gc] == 'a':
                    cells[i][gc] = 'g'

        # Count unguarded cells
        res = 0
        for i in range(m):
            for j in range(n):
                if cells[i][j] == 'a':
                    res += 1
        return res

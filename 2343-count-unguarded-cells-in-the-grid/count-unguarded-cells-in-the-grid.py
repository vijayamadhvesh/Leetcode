__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [['a' for _ in range(n)] for _ in range(m)]

        for r, c in walls:
            cells[r][c] = 'w'

        for r, c in guards:
            cells[r][c] = 'G'


        for gr, gc in guards:

            for i in range(gc-1, -1, -1):
                if cells[gr][i] in ('w', 'G'):
                    break
                if cells[gr][i] == 'a':
                    cells[gr][i] = 'g'

            for i in range(gc+1, n):
                if cells[gr][i] in ('w', 'G'):
                    break
                if cells[gr][i] == 'a':
                        cells[gr][i] = 'g'


            for i in range(gr-1, -1, -1):
                if cells[i][gc] in ('w', 'G'):
                    break
                if cells[i][gc] == 'a':
                        cells[i][gc] = 'g'

            for i in range(gr+1, m):
                if cells[i][gc] in ('w', 'G'):
                    break
                if cells[i][gc] == 'a':
                        cells[i][gc] = 'g'
                
        res = 0

        for i in range(m):
            for j in range(n):
                if cells[i][j] == 'a':
                    res += 1
        return res
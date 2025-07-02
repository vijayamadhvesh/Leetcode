class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [set() for _ in range(9)]
        squares = collections.defaultdict(set)

        for i in range(9):
            row = set()
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in row or val in cols[j] or val in squares[(i//3, j//3)]:
                    return False
                row.add(val)
                cols[j].add(val)
                squares[(i//3, j//3)].add(val)
        return True
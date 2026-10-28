class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        n = [[0] * 9 for _ in range(9)]
        for i, r in enumerate(board):
            c = 9 * [0]
            for j, s in enumerate(r):
                if s == '.':
                    continue
                v = int(s)-1
                if m[i//3][j//3][v] or n[j][v] or c[v]:
                    return False
                m[i//3][j//3][v] = 1
                n[j][v] = 1
                c[v] = 1
        return True
            
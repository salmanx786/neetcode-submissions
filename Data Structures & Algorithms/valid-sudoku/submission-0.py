class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # going through rows and columns
        for i in range(len(board)):
            seen = set()
            seenc = set()

            for j in range(len(board)):
                if board[i][j] in seen:
                    return False
                if board[j][i] in seenc:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
                if board[j][i] != ".":
                    seenc.add(board[j][i])
        # going through boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                box = set()
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        if board[r][c] in box:
                            return False
                        if board[r][c] != ".":
                            box.add(board[r][c])

        return True

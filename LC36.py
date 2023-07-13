class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if (char != '.'):
                    row = char + " found in row " + str(i)
                    col = char + " found in col " + str(j)
                    box = char + " found in box " + str(i//3) + "-" +  str(j//3)
                    if (row in seen or col in seen or box in seen):
                        return False
                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        return True
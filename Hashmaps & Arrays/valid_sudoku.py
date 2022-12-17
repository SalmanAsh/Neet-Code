import collections


class Sudoku:
    """Method-one"""

    def validation(self, board: list[list[str]]) -> bool:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(board)):
            hashset = set()
            for j in range(len(board[i])):
                if board[i][j] in nums and board[i][j] in hashset:
                    return False
                elif board[i][j] in nums:
                    hashset.add(board[i][j])

        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(board)):
            hashset = set()
            for j in range(len(board[i])):
                if board[i][j] in nums and board[i][j] in hashset:
                    return False
                elif board[i][j] in nums:
                    hashset.add(board[i][j])

        return True


class Sudoku:
    """Method-two"""

    def validation(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)  # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqrs[r//3, c//3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[r//3, c//3].add(board[r][c])

        return True


test = Sudoku()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(test.validation(board))

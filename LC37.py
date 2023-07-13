class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if (char != '.'):
                    row = char + " found in row " + str(i)
                    col = char + " found in col " + str(j)
                    box = char + " found in box " + str(i//3) + "-" +  str(j//3)
                    if (row in seen or col in seen or box in seen):
                        continue
                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        
        def backtrack(i, j):
            nonlocal solved
            if i == 9:
                solved = True
                return

            new_i = i + (j + 1) // 9
            new_j = (j + 1) % 9

            if board[i][j] != '.':
                backtrack(new_i, new_j)
            else: 
                for num in range(1, 10):
                    num = str(num)
                    row = num + " found in row " + str(i)
                    col = num + " found in col " + str(j)
                    box = num + " found in box " + str(i//3) + "-" +  str(j//3)
                    if (row not in seen and col not in seen and box not in seen):
                        board[i][j] == num
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)

                        backtrack(new_i, new_j)
                        if not solved:
                            seen.remove(row)
                            seen.remove(col)
                            seen.remove(box)
                            board[i][j] = '.'
                    
        solved = False
        backtrack(0, 0)
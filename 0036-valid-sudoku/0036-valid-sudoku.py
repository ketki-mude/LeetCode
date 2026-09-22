class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # 1. Check rows
        for i in range(9):
            seen = set()

            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # 2. Check columns
        for i in range(9):
            seen = set()

            for j in range(9):
                value = board[j][i]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # 3. Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                seen = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        value = board[i][j]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Set first column value in each row
        for i in range(m):
            if grid[i][0] == 0:
                # Flip that row
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]  # Flipping

        for j in range(1, n):
            countZero = 0
            for i in range(m):
                if grid[i][j] == 0:
                    countZero += 1

            countOne = m - countZero
            if countZero > countOne:
                # Flipping that column
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        score = 0
        for i in range(m):
            for j in range(n):
                value = grid[i][j] * pow(2, n - j - 1)
                score += value

        return score

        
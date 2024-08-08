class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [
            (0, 1),   # EAST
            (1, 0),   # SOUTH
            (0, -1),  # WEST
            (-1, 0)   # NORTH
        ]

        result = []
        step = 0  # how many steps to move
        dir = 0   # which direction

        result.append([rStart, cStart])

        while len(result) < rows * cols:
            if dir == 0 or dir == 2:
                step += 1

            for _ in range(step):
                rStart += directions[dir][0]
                cStart += directions[dir][1]

                if 0 <= rStart < rows and 0 <= cStart < cols:  # check valid
                    result.append([rStart, cStart])

            dir = (dir + 1) % 4  # turn to the next direction

        return result
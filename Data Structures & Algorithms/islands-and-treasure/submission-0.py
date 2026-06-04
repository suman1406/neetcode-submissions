from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        if not grid:
            return

        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = {
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        }

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or
                    nc < 0 or
                    nr >= rows or
                    nc >= cols
                ):
                    continue

                if grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[r][c] + 1

                q.append((nr, nc))
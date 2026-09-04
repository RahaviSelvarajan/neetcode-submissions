# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         rows, cols = len(grid), len(grid[0])
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         def bfs(r, c):
#             visited = set()
#             visited.add((r,c))
#             res = 2147483647
#             q = deque([(0, r, c)])
#             while q:
#                 dist, row, col = q.popleft()
#                 for dr, dc in directions:
#                     nr, nc = row + dr, col + dc
#                     if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
#                         if grid[nr][nc] == 2147483647:
#                             q.append((dist + 1, nr, nc))
#                             visited.add((nr, nc))
#                         elif 0 <= grid[nr][nc] < 2147483647:
#                             res = min(res, grid[nr][nc] + dist + 1)
#             return res

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2147483647:
#                     grid[r][c] = bfs(r,c)
#         return
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
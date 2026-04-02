class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        m, n = len(grid), len(grid[0])
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                distance = 0
                if grid[i][j]==0:
                    queue.append((i, j, 0))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while queue:
            r, c, level = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    queue.append((nr, nc, level + 1))
                    grid[nr][nc] = level + 1

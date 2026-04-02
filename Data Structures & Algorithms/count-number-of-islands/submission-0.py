class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "-1"
                    queue.append((i,j))
                    while (queue):
                        r, c  = queue.popleft()
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                                queue.append((nr,nc))
                                grid[nr][nc] = "-1"
                    num_islands += 1
        return num_islands
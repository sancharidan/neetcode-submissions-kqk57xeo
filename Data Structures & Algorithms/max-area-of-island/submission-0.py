class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        max_area = 0
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for i in range(m):
            for j in range(n):
                area = 0
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = -1
                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]==1:
                                queue.append((nr, nc))
                                grid[nr][nc] = -1
                        
                        area += 1
                    if area > max_area:
                        max_area = area
        return max_area


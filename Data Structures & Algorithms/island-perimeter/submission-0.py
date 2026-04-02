class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = -1
                    while queue:
                        r, c = queue.popleft()

                        if r == 0:
                            perimeter += 1
                        if r == m-1:
                            perimeter += 1
                        if c == 0:
                            perimeter += 1
                        if c == n-1:
                            perimeter += 1
                        if c+1 < n and grid[r][c+1]==0:
                            perimeter += 1
                        if r+1 < m and grid[r+1][c]==0:
                            perimeter += 1
                        if c-1 >= 0 and grid[r][c-1]==0:
                            perimeter += 1
                        if r-1 >=0 and grid[r-1][c]==0:
                            perimeter += 1

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]==1:
                                queue.append((nr, nc))
                                grid[nr][nc] = -1
                            
        return perimeter


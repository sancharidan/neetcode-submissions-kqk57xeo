class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()

        directions = [(0, 1), (1, 0), (0, -1), (-1,0)]

        cntFresh = 0
        rotten = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    cntFresh += 1

        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    queue.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    rotten += 1
        
            if rotten == cntFresh != 0:
                return time + 1
        if rotten == cntFresh == 0:
            return 0
        return -1
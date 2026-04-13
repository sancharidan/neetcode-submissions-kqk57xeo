class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        m, n = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pacific_queue.append((i,j))
                    pacific.add((i,j))

        while pacific_queue:
            r, c = pacific_queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in pacific and heights[nr][nc]>=heights[r][c]):
                    pacific_queue.append((nr,nc))
                    pacific.add((nr,nc))


        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    atlantic_queue.append((i,j))
                    atlantic.add((i,j))

        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < m and 0 <= nc < n and heights[nr][nc]>=heights[r][c] and (nr, nc) not in atlantic):
                    atlantic_queue.append((nr,nc))
                    atlantic.add((nr,nc))

        return [list(cell) for cell in pacific.intersection(atlantic)]



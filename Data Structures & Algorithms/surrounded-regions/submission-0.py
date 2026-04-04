class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j]=='O':
                    queue.append((i,j))
        print (queue)

        while queue:
            r, c = queue.popleft()
            board[r][c] = 'T'
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    queue.append((nr, nc))
                    board[nr][nc] = 'T'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


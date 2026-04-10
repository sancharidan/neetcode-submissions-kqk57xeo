class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        adj_list = {i: [] for i in range(n)}
        visited = set()
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
    
        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    queue.extend(adj_list[node])

        num_components = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                num_components += 1
        return num_components


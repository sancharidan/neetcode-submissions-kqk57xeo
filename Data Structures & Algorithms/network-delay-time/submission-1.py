class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            adj_list[u].append((v, w))
        print (adj_list)
        minheap = [(0, k)]
        times = [1e09] * (n + 1)
        times[k] = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            for node, weight in adj_list[n1]:
                if w1 + weight < times[node]:
                    times[node] = w1 + weight
                    heapq.heappush(minheap, (w1 + weight, node))

        times = times[1:]
        if max(times) == 1e09:
            return -1
        else:
            return max(times)


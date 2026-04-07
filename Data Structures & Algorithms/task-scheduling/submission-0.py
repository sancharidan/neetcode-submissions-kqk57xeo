class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        time = 0
        maxheap = []
        queue = deque()
        for key, val in freqMap.items():
            heapq.heappush(maxheap, (-val))
        
        while maxheap or queue:
            time += 1
            if maxheap:
                freq = heapq.heappop(maxheap)
                remaining_count = -freq
                remaining_count -= 1
                if remaining_count > 0:
                    queue.append((remaining_count, time + n))

            if queue:
                if queue[0][1] == time:
                    remaining_count, next_available_time = queue.popleft()
                    heapq.heappush(maxheap, -remaining_count)
        
        return time
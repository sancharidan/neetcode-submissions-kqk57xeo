class Solution:
    def distance(x1, y1, x2, y2):
        return (sqrt((x1 - x2)^2 + (y1 - y2)^2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap with size k implementation
        maxHeap = []
        res = []
        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y]) 

        return res

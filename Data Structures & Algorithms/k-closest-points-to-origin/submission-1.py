class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap with size k implementation
        maxHeap = []
        res = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y]) 

        return res
        # return [[x, y] for (_, x, y) in maxHeap]

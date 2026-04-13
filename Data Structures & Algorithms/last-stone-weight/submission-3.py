class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-weight for weight in stones]
        heapq.heapify(weights)
        while weights:
            if len(weights) == 1:
                return -weights[0]
            y = -heapq.heappop(weights)
            x = -heapq.heappop(weights)
            y = abs(y-x)
            heapq.heappush(weights, -y)
        return 0

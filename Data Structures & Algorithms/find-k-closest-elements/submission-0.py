class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = [abs(elem - x) for elem in arr]
        maxheap = []
        for i in range(len(arr)):
            heapq.heappush(maxheap, (-distances[i], -arr[i]))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return sorted([-elem for dist, elem in maxheap])
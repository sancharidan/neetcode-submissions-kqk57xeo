"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda x: x.start)
        minheap = []
        for interval in intervals:
            currStart = interval.start
            currEnd = interval.end
            if minheap:
                if currStart >= minheap[0]:
                    heapq.heappop(minheap)
            heapq.heappush(minheap, currEnd)
            
        return len(minheap)
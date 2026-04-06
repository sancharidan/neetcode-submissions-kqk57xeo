from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        minHeap = []
        for num, freq in count_map.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # return [num for freq, num in minHeap]
        res = []
        for freq, num in minHeap:
            res.append(num)
        return res
        

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = [[] for i in range(len(nums) + 1)]
#         count_map = {}
#         for num in nums:
#             count_map[num] = 1 + count_map.get(num, 0)
#         for key,val in count_map.items():
#             freq[val].append(key)
#         print (freq)
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res)==k:
#                     return res
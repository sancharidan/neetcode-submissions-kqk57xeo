from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         c = Counter(nums)
#         return [t[0] for t in c.most_common(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        for key,val in count_map.items():
            freq[val].append(key)
        print (freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
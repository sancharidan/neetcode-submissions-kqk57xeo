class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        for num in nums_set:
            length = 0
            if num-1 not in nums_set:
                length = 1
                while num+length in nums_set:
                    length+=1
            if length>maxlen:
                maxlen = length
        return maxlen

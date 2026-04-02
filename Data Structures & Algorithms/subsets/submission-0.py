class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def find(arr, idx):
            if idx == len(nums):
                res.append(arr[:])
                return
            arr.append(nums[idx])
            find(arr, idx + 1) # pick

            arr.pop()
            find(arr, idx + 1) # not pick
        find([],0)
        return res
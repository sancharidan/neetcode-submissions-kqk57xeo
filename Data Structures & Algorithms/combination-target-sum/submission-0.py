class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def find_comb(arr, idx, sums):
            if sums == target:
                res.append(arr[:])
                print (arr[:])
                return
            if sums>target or idx==len(nums):
                return
            # pick
            arr.append(nums[idx])
            sums += nums[idx]
            find_comb(arr, idx, sums)
            
            # not pick
            sums -= nums[idx]
            arr.pop()
            find_comb(arr, idx + 1, sums)

        find_comb([],0,0)
        return res
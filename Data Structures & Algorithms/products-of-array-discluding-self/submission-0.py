class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = []
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        pre = 1
        for i in range(1, len(nums)):
            pre = pre * nums[i-1]
            prefix[i] = pre
        suf = 1
        for i in range(len(nums)-2,-1,-1):
            suf = suf * nums[i+1]
            suffix[i] = suf
        outputs = [p*f for p,f in zip(prefix,suffix)]
        return outputs
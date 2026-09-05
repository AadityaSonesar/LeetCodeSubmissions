class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max=nums[0]
        sufix_min=[0]*len(nums)
        sufix_min[-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            sufix_min[i]=min(sufix_min[i+1],nums[i])

        for i in range(len(nums)):
            prefix_max=max(prefix_max,nums[i])

            if prefix_max-sufix_min[i]<=k:
                return i

        return -1
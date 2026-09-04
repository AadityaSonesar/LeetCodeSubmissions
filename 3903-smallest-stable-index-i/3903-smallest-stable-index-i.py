class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefixMax=nums[0]
        sufixMin=[0]*len(nums)
        sufixMin[-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            sufixMin[i]=min(nums[i],sufixMin[i+1])

        for i in range(len(nums)):
            prefixMax=max(prefixMax,nums[i])

            if prefixMax-sufixMin[i]<=k:
                return i

            
        return -1
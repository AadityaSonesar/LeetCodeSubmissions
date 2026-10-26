class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap={}
        for i in range(len(nums)):
            if target-nums[i] in numMap:
                return [i,numMap[target-nums[i]]]
            
            numMap[nums[i]]=i
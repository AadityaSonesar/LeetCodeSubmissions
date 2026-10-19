class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        index=[]
        for i in range(len(nums)):
            if nums[i]>target:
                break
            if nums[i]==target:
                index.append(i)
        return index

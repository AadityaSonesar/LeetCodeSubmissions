class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k,i =1, 1
        for i in range(len(nums)):
            if nums[i]>nums[k-1]:
                nums[i], nums[k]= nums[k], nums[i]
                k+=1
        return k

        
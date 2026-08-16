class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k=0, 0, 0
        while i<len(nums):
            k=nums[i]
            j=0
            while i<len(nums) and nums[i]==k :
                if j<2:
                    j+=1
                    i+=1
                else:
                    nums.pop(i)

            

        return len(nums)
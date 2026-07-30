class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        temp=0
        length=len(nums)
        for i in range(0, length):
            if nums[i]==1:
                temp+=1
                if count<temp:
                    count= temp
            else: temp=0
        return count
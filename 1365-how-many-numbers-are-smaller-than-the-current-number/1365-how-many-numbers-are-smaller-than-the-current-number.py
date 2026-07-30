class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallnums=[]
        for i in nums:
            smaller=0
            for j in nums:
                if j<i:
                    smaller+=1
            smallnums.append(smaller)
        return smallnums
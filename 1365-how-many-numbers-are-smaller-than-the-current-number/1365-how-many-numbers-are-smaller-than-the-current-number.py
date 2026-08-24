class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter=[0]*101
        smaller=[0]*101
        ans=[]
        for num in nums:
            counter[num]+=1

        for i in range(1,len(counter)):
            smaller[i]=smaller[i-1]+counter[i-1]

        for num in nums:
            ans.append(smaller[num])

        return ans
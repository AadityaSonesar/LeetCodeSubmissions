class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing,duplicate=0,0
        seennums=set()
        #finding duplicates
        for i in nums:
            if i not in seennums:
                seennums.add(i)
            else:
                duplicate=i
        
        #finding missing num
        for i in range(1,len(nums)+1):
            if i not in seennums:
                missing=i

        return [duplicate,missing]

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared=list(map(lambda x: x**2,nums))

        squared.sort()

        i=0
        j=len(nums)-1
        ans=0
        
        while i<=j:
            ans+=squared[j]
            if i==j:
                break
            ans-=squared[i]
            print("i=")
            j-= 1
            i+=1
        #ans+=squared[j]
        return ans
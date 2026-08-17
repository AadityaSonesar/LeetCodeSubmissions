class Solution:
    def reverse(self,nums, left, right):
        while left<right:
            nums[left], nums[right]=nums[right], nums[left]
            left+=1
            right-=1

    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
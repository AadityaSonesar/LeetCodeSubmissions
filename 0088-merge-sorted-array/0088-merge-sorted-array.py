class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged=sorted(nums1[:m]+nums2)
        for i in range(m+n):
            nums1[i]=merged[i]
        print(nums1)
        
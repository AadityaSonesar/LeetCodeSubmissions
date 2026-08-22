class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies)
        flags=[]
        for i in candies:
            if i+extraCandies>=greatest:
                flags.append(True)
            else:
                flags.append(False)

        return flags
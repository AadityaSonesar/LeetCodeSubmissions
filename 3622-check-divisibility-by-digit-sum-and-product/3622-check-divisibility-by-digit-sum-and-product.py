class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums=0
        product=1
        for d in str(n):
            sums+=int(d)
            product*=int(d)

        return n%(sums+product)==0
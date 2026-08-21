class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        product=1
        for d in str(n):
            product*=int(d)
            sums+=int(d)

        return product-sums
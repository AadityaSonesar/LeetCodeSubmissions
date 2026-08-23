class Solution:
    def countDigits(self, num: int) -> int:
        counter=0
        for d in str(num):
            if num%int(d)==0:
                counter+=1

        return counter
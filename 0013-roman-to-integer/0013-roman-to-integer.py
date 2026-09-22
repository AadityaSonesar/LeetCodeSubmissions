class Solution:
    def romanToInt(self, s: str) -> int:
        values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num=0
        i=len(s)-1
        while i>0:
            if values[s[i-1]]<values[s[i]]:
                num+=(values[s[i]]-values[s[i-1]])
                i-=2
            else:
                num+=values[s[i]]
                i-=1
        if i==0:
            num+=values[s[0]]
        return num
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        string=""
        right=len(s)-1
        for i in range(len(s)-2,-1,-1):
            if s[i]!=" ":
                continue

            if i>0 and s[i-1]==" ":
                continue

            string+=s[i+1:right+1].strip()+" "
            right=i-1
            
                
            
        string+=s[0:right+1]

        return string
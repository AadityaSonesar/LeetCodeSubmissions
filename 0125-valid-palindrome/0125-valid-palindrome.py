class Solution:
    s=""
    def pal(self,l: int, r:int) -> bool:
        if l>=r:
            return True
        if not self.s[l].isalnum():
            return self.pal(l+1,r)
        if not self.s[r].isalnum():
            return self.pal(l,r-1)
        if self.s[l].lower() != self.s[r].lower():
            return False
        else:
            return self.pal(l+1, r-1)  

    def isPalindrome(self, s: str) -> bool:
        self.s=s
        return self.pal(0,len(s)-1)
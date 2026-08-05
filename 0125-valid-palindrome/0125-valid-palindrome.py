class Solution:
    def pal(self,s: str, l: int, r:int) -> bool:
        if l>=r:
            return True
        if not s[l].isalnum():
            return self.pal(s,l+1,r)
        if not s[r].isalnum():
            return self.pal(s,l,r-1)
        if s[l].lower() != s[r].lower():
            return False
        return self.pal(s, l+1, r-1)  

    def isPalindrome(self, s: str) -> bool:
        return self.pal(s,0,len(s)-1)
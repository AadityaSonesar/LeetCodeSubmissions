class Solution:
    def hIndex(self, citations: List[int]) -> int:
        index=0
        for i in range(1,len(citations)+1):
            counter=0
            for j in citations:
                if j>=i:
                    counter+=1
            if i<=counter:
                index=i
            
        return index
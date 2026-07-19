class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        targetLen=len(target)
        targetIndex=0
        for i in range(1,n+1):
            stack.append("Push")
            if i==target[targetIndex]:
                targetIndex+=1
            else:
                stack.append("Pop")
            if targetLen==targetIndex:
                break
        return stack
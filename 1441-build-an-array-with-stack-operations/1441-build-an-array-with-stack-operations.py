class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetSet=set(target)
        stackNum=[]
        stack=[]
        targetLen=len(targetSet)
        for i in range(1,n+1):
            stack.append("Push")
            stackNum.append(i)
            if i not in targetSet:
                stack.append("Pop")
                stackNum.pop()
            if targetLen==len(stackNum):
                break
        return stack
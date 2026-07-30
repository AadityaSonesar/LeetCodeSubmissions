class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        prevTime=0
        ans=[0]*n
        for i in logs:
            fid, status, time=i.split(":")
            
            if status=="start":
                if len(stack)!=0:
                    ans[int(stack[-1])]+=int(time)-prevTime
                prevTime=int(time)
                stack.append(int(fid))
            else:
                if len(stack)!=0:
                    ans[int(stack[-1])]+=int(time)-prevTime+1
                prevTime=int(time)+1
                stack.pop()
        return ans
                
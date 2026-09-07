class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        current_gas=0
        if sum(gas)>=sum(cost):
            for i in range(len(gas)):
                if current_gas<0:
                    start=i
                    current_gas=0
                current_gas+=gas[i]-cost[i]

            return start
                
        else:
            return -1
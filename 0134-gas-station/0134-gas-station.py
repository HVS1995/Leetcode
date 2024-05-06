class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank,curr_tank = 0,0
        start_station = 0
        n = len(gas)
        for i in range(n):
            diff  = gas[i] - cost[i]
            total_tank +=diff
            curr_tank +=diff
            
            if curr_tank < 0:
                curr_tank =0
                start_station = i+1
        if total_tank >= 0:
            return start_station
        else:
            return -1
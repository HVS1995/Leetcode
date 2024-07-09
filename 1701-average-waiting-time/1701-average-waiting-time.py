from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        totalWaitTime = 0
        currTime = 0

        for customer in customers:
            arrivalTime = customer[0]
            cookTime = customer[1]

            if currTime < arrivalTime:
                currTime = arrivalTime

            waitTime = currTime + cookTime - arrivalTime

            totalWaitTime += waitTime

            currTime += cookTime

        return totalWaitTime / n
        
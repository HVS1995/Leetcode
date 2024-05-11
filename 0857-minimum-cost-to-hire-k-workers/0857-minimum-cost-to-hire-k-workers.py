from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], min_wage: List[int], k: int) -> float:
        n = len(quality)

        worker_ratio = [(min_wage[i] / quality[i], quality[i]) for i in range(n)]
        worker_ratio.sort()

        pq = []
        sum_quality = 0

        for i in range(k):
            heapq.heappush(pq, -worker_ratio[i][1])  # Push all qualities in max-heap
            sum_quality += worker_ratio[i][1]  # Find sum of qualities

        manager_ratio = worker_ratio[k - 1][0]
        result = manager_ratio * sum_quality

        for manager in range(k, n):
            manager_ratio = worker_ratio[manager][0]

            heapq.heappush(pq, -worker_ratio[manager][1])  # Push the quality of the new worker in max-heap
            sum_quality += worker_ratio[manager][1]  # Find sum of qualities

            if len(pq) > k:
                sum_quality += heapq.heappop(pq)

            result = min(result, manager_ratio * sum_quality)

        return result
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                div = arr[i] / arr[j]
                heapq.heappush(pq, (-div, arr[i], arr[j]))
                if len(pq) > k:
                    heapq.heappop(pq)
        
        vec = heapq.heappop(pq)
        result = [vec[1], vec[2]]
        return result
        
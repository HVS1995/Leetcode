class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        total = 0
        min_length = float('inf')
        
        while j < len(nums):
            total += nums[j]
            while total >= target:
                min_length = min(min_length, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1
        
        if min_length == float('inf'):
            return 0
        return min_length
                
        
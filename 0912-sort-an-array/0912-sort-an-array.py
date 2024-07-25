from typing import List
from collections import defaultdict

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minE = min(nums)
        maxE = max(nums)
        
        mp = defaultdict(int)
        
        for num in nums:
            mp[num] += 1
        
        i = 0
        
        for num in range(minE, maxE + 1):
            while mp[num] > 0:
                nums[i] = num
                i += 1
                mp[num] -= 1
        
        return nums

    
        
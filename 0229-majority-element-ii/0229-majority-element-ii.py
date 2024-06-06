from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        maj1 = None
        count1 = 0
        
        maj2 = None
        count2 = 0
        
        for i in range(n):
            if nums[i] == maj1:
                count1 += 1
                
            elif nums[i] == maj2:
                count2 += 1 
                
            elif count1 == 0:
                maj1 = nums[i]
                count1 = 1
                
            elif count2 == 0:
                maj2 = nums[i]
                count2 = 1
                
            else:
                count1 -= 1
                count2 -= 1
                
        result = []
        count1 = 0
        count2 = 0

        for num in nums:
            if num == maj1:
                count1 += 1
            elif num == maj2:
                count2 += 1

        if count1 > n // 3:
            result.append(maj1)
        if count2 > n // 3:
            result.append(maj2)

        return result
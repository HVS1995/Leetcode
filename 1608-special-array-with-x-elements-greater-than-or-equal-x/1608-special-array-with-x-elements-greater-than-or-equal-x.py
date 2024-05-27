class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        for x in range(N+1):
            count =  sum(1 for num in nums if num >= x)
            if count == x:
                return x
                
        return -1
            
                
           
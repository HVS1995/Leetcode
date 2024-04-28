
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        difference = nums2[0] - nums1[0]
        
        for i in range(1,len(nums1)):
            if nums2[i] - nums1[i] != difference:
                return 0
            
        return difference
            
        
       
           
        
          
        
       
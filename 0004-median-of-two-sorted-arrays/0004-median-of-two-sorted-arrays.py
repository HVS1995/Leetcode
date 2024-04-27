class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        i,j =0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merge.append(nums1[i])
                i +=1
                
            else:
                merge.append(nums2[j])
                j +=1
                
        while i < len(nums1):
            merge.append(nums1[i])
            i += 1
    
        while j < len(nums2):
            merge.append(nums2[j])
            j += 1
    
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            median_index1 = total_len // 2 - 1
            median_index2 = total_len // 2
            median = (merge[median_index1] + merge[median_index2]) / 2
        else:
            median_index = total_len // 2
            median = merge[median_index]
    
        return median 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        # Perform binary search
        while low <= high:
            mid = (low + high) // 2
            
            # If target is found at mid, return mid index
            if nums[mid] == target:
                return mid
            
            # Check which half of the array is sorted
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    # If target is in the left half, adjust high pointer
                    high = mid - 1
                else:
                    # Otherwise, adjust low pointer
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    # If target is in the right half, adjust low pointer
                    low = mid + 1
                else:
                    # Otherwise, adjust high pointer
                    high = mid - 1
        
        # If target is not found, return -1
        return -1
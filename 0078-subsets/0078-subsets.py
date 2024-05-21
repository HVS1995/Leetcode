class Solution:
    def __init__(self):
        self.result = []

    def solve(self, nums: List[int], idx: int, temp: List[int]):
        if idx >= len(nums):
            self.result.append(temp.copy())
            return

        # Include the current element
        temp.append(nums[idx])
        self.solve(nums, idx + 1, temp)

        # Exclude the current element
        temp.pop()
        self.solve(nums, idx + 1, temp)
    
    
    
    
    
    
    
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        self.result = []
        self.solve(nums,0,temp)
        return self.result
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxi = nums[0]
        sum = 0
        
        for num in nums:
            sum += num
            maxi = max(maxi, sum)
            if sum < 0:
                sum = 0
                
        return maxi if maxi > 0 else max(nums)
        
        
        # cur_max, max_till_now = 0, -inf
        # for c in nums:
        #     cur_max = max(c, cur_max + c)
        #     max_till_now = max(max_till_now, cur_max)
        # return max_till_now 
class Solution:
    def leftmax(self,height):
        n = len(height)
        leftmax = [0]*n
        leftmax[0] = height[0]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        return leftmax
    
    
    def rightmax(self,height):
        n = len(height)
        rightmax = [0]*n
        rightmax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])
        return rightmax
            
    
    
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 or n == 1:
            return 0
        leftmax = self.leftmax(height)
        rightmax = self.rightmax(height)
        
        sum = 0
        for i in range(n):
            sum += min(leftmax[i], rightmax[i]) - height[i]
            
        return sum
    
        
        
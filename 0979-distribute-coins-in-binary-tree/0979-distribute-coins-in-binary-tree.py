# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # Calculate total excess or deficit in the subtree rooted at the current node
            total_excess = node.val + left_excess + right_excess - 1
            
            # Accumulate the total number of moves required
            self.moves += abs(total_excess)
            
            # Return the excess or deficit of coins in the subtree rooted at the current node
            return total_excess
        
        dfs(root)
        return self.moves
        
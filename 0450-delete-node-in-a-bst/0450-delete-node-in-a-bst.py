# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getsucc(self,root):
        while root.left is not None:
            root = root.left

        return root.val




    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                succ = self.getsucc(root.right)
                root.val = succ
                root.right = self.deleteNode(root.right,succ)
        return root
        
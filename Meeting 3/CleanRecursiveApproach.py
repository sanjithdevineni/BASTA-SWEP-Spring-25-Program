# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf')) # using negative and positive infinity


    def validate(self, node, minVal, maxVal):
        if node is None: # if node doesn't exist, entire subtree is valid
            return True
        
        if node.val <= minVal or node.val >= maxVal: # immediately invalidate if error found
            return False
        
        return self.validate(node.left, minVal, node.val) and self.validate(node.right, node.val, maxVal)
        

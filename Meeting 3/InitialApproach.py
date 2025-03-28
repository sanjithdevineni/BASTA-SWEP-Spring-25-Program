# import requests
# import mysql.connector
# import pandas as pd

# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        
        # def function(root, )
        # base case: check if node is null
        # recursive case: check if left node is less than root, traverse left subtree
        # if not, return false
        # visit node: if its valid
        # check if right node is greater than root, traverse right subtree
        # if not, return false
        
        # return true at the end
        
        result = self.traverse(root)
        return result
        
        def traverse(root) -> bool:
            if root.val is None:
                return True
            
            if (root.left.val > or root.right.val < )
              return False
            
            return (LeftSubtree And rightSubtree)
            
            # if root.left.val is None or root.left.val < root.val:
            #     if not traverse(root.left):
            #         return False
            # else:
            #     return False
            # if root.right.val is None or root.right.val > root.val:
            #     if not traverse(root.right):
            #         return False
            # else:
            #     return False
            
            
            # return True
            
            
            
            
        #     5
        #    / \
        #   1   6
        #      / \
        #     2   7

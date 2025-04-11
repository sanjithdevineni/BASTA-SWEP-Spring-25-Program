# import requests
# import mysql.connector
# import pandas as pd

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # use dfs(node)
        # base case: if node is either p or q, return node
        # recursive step: recurse left and store return value, then recurse right 
        # return current node in the case that both left and right subtrees are not null
        
        def dfs(node):
            if node is None:
                return None
            elif node == p or node == q:
                return node
                
            leftsubtree = dfs(node.left)
            rightsubtree = dfs(node.right)
            
            if leftsubtree is not None and rightsubtree is not None:
                return node
            elif rightsubtree is None:
                return leftsubtree
            else:
                return rightsubtree
            
        return dfs(root)
        
        # Time complexity: O(n)
        # Space complexity: O(n)
        



        # use dfs(node)
        # base case: if node is either p or q, return node
        # recursive step: recurse left and store return value, then recurse right 
        # return current node in the case that both left and right subtrees are not null
        
        def dfs(node):
            if node is None:
                return None
            elif node == p or node == q:
                return node
                
            leftsubtree = dfs(node.left)
            rightsubtree = dfs(node.right)
            
            if leftsubtree is not None and rightsubtree is not None:
                return node
            elif rightsubtree is None:
                return leftsubtree
            else:
                return rightsubtree
            
        return dfs(root)
        
        # Time complexity: O(n)
        # Space complexity: O(n)

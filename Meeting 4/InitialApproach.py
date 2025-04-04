# import requests
# import mysql.connector
# import pandas as pd

# https://leetcode.com/problems/number-of-islands/description/ 


# Time complexity:
# Space Complexity: 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use DFS to find all the clusters of 1s
        # When the DFS finds an edge or finds a 0, then it we've hit water.
        
        solution = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    solution += 1
        return solution
        
        
    def dfs(self, ver, hor, grid):
        if ver < 0 or ver >= len(grid) or hor < 0 or hor >= len(grid[0]):
            return
        elif grid[ver][hor] == '0' or grid[ver][hor] == '2':
            return
        grid[ver][hor] = '2'
            
        self.dfs(ver+1, hor, grid)
        self.dfs(ver-1, hor, grid)
        self.dfs(ver, hor+1, grid)
        self.dfs(ver, hor-1, grid)
        
        
        
        # grid = [
#   ["2","2","2","2","0"],
#   ["2","2","0","2","0"],
#   ["2","2","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
        
        # Time complexity: O(n * m)
        
        # Space complexity: O(n * m) (or constant, depending on how you define it)



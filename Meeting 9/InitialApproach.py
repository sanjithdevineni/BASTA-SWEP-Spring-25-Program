# import requests
# import mysql.connector
# import pandas as pd

# https://leetcode.com/problems/min-cost-climbing-stairs/

# [1, 5, 3, 6]

# 0 - 2 - <end>
# 0 - 1 - 3 - <end>

# sum[0] = cost[0]
# sum[1] = cost[1]
# sum[2] = cost[2] + min(sum[0], sum[1])
# sum[3] = cost[3] + min(sum[1], sum[2])

# return min(sum[8], sum[9])

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # initialize sum with length equal to len(cost)
        # assign cost[0] to sum[0]
        # assign cost[1] to sum[1]
        
        # for i -> 2, len(cost):
        # sum[i] = cost[i] + min(sum[i-2], sum[i-1])
        
        # return min(sum[-1], sum[-2])
        
        sum = [0] * len(cost)
        
        sum[0] = cost[0]
        sum[1] = cost[1]
        
        for i in range(2, len(cost)):
            sum[i] = cost[i] + min(sum[i-2], sum[i-1])
            
        return min(sum[-1], sum[-2])
        
        
# Time complexity: O(n)
# Space complexity: O(n)

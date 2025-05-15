# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def min_cost(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            memo[i] = cost[i] + min(min_cost(i - 1), min_cost(i - 2))
            return memo[i]

        return min(min_cost(n - 1), min_cost(n - 2))

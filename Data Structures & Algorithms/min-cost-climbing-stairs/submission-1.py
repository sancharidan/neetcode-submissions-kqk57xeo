class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recur(ind):
            if ind == 0 or ind == 1:
                return 0
            small = recur(ind - 1) + cost[ind - 1]
            large = recur(ind - 2) + cost[ind - 2]
            return (min(small, large))
        return recur(len(cost))
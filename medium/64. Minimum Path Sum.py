from torch import grid_sampler


class Solution:
    def minPathSum(self, grid) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[10e4]*n for _ in range(m)] 
        dp[0][0] = grid[0][0]

        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1, n):
                if dp[i-1][j]<dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    
        return dp[-1][-1]



grid = [[1,3,1],[1,5,1],[4,2,1]]
print('Output', Solution().minPathSum(grid))
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

grid = [[1,2,3],[4,5,6]]
print('Output', Solution().minPathSum(grid))
# Output: 12

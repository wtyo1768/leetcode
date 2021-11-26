
# Time limited sol
class Solution:
    def helper(self, m, n):
        # print(m, n)
        if m==1 and n==1:
            # print('f')
            self.ans = self.ans + 1
        if m-1>=1:
            self.helper(m-1, n)
        if n-1>=1:
            self.helper(m, n-1)

    def uniquePaths(self, m: int, n: int) -> int:
        self.ans = 0
        
        self.helper(m, n)

        return self.ans


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


m = 3
n = 7
# Output: 28
print('Output:', Solution().uniquePaths(m, n))


m = 3
n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
print('Output:', Solution().uniquePaths(m, n))



m = 7
n = 3
# Output: 28
print('Output:', Solution().uniquePaths(m, n))



m = 3
n = 3
# Output: 6
print('Output:', Solution().uniquePaths(m, n))

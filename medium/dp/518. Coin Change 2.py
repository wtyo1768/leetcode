

class Solution:
    def change(self, amount: int, coins) -> int:
        
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for t in range(coin, amount+1):
                dp[t] += dp[t-coin]
        print(dp)
        return dp[amount]


amount = 5
coins = [1,2,5]
print('Output :', Solution().change(amount, coins))
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

amount = 3
coins = [2]
print('Output :', Solution().change(amount, coins))
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

amount = 10
coins = [10]
print('Output :', Solution().change(amount, coins))
# Output: 1

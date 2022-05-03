


class Solution:
    def combinationSum4(self, cand, target):  
        dp = [0] * (target+1)
        dp[0] = 1 

        for t in range(1, target+1):
            for num in cand:
                if num<=t:
                    dp[t] += dp[t-num]
        return dp[-1]


nums = [1,2,3]
target = 4
print('Output: ', Solution().combinationSum4(nums, target))
# Output: 7

nums = [9]
target = 3
print('Output: ', Solution().combinationSum4(nums, target))
# Output: 0

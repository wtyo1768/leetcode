

from ctypes.wintypes import tagMSG


class Solution:
    def canPartition(self, nums) -> bool:
        
        target = sum(nums) / 2

        if not target.is_integer() or len(nums)<=1: return False
        target = int(target)

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for t in range(target, -1, -1):
                dp[t] = dp[t] or dp[t-num]
        # print(dp)
        return dp[-1]



class Solution:
    def canPartition(self, nums) -> bool:
        
        target = sum(nums) / 2

        if not target.is_integer(): return False

        target = int(target)
        dp = [False] * (target+1)
        dp[0] = True

        
        for num in nums:
            for t in range(target, num-1, -1):
                dp[t] = dp[t-num] or dp[t]

        return dp[-1]



nums = [1,5,11,5]
# Output: true
print('Output :', Solution().canPartition(nums))



nums = [1,2,3,5]
# Output: false
print('Output :', Solution().canPartition(nums))


nums = [1,2,5]
# Output: false
print('Output :', Solution().canPartition(nums))







### n^2 Sol
class n_square_Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = [1] * m
        for i in range(m-2, -1, -1):
            for j in range(i+1, m):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


from  bisect import bisect_left
### n*log(n) Sol
class Solution(object):
    def bfs(nums):
        

        pass
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = [1] * m
        for i in range(m-2, -1, -1):
            # for j in range(i+1, m):
            if nums[i] < nums[i-1]:
                dp[i] = dp[i+1] +1
            else:
                idx = bisect_left(nums[i+1:], nums[i])

                nums[idx], nums[i] = nums[i], nums[idx]

            #     dp[i] = max(dp[i], dp[j]+1)
            # else:
                







        return max(dp)





nums = [10,9,2,5,3,7,101,18]

Output: 4
output = Solution().lengthOfLIS(nums)
print('Output', output)

nums = [0,1,0,3,2,3]

Output: 4
output = Solution().lengthOfLIS(nums)
print('Output', output)

nums = [7,7,7,7,7,7,7]

Output: 1
output = Solution().lengthOfLIS(nums)
print('Output', output)
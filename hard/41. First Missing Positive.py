

class Solution:
    def firstMissingPositive(self, nums) -> int:
        
        nums.append(0)
        n = len(nums)
        
        for i in range(n):
            if nums[i]>=n or nums[i]<0:nums[i] = 0
            
        for i in range(n):
            nums[nums[i]%n] += n

        for i in range(1, n):
            if nums[i]//n==0:return i
        return n


nums = [0, 3]
print('Output', Solution().firstMissingPositive(nums))
# Output: 3

nums = [3,4,-1,1]
print('Output', Solution().firstMissingPositive(nums))
# Output: 2

print('Output', Solution().firstMissingPositive(nums))
nums = [7,8,9,11,12]
# Output: 1

        
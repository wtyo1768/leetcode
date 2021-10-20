


#HASH

class Solution:
    def twoSum(self, nums, target: int):
        i = 0
        j = len(nums)-1 

        while(i<j):
            s = nums[i]+nums[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1, j+1]



nums = [2,7,11,15]
target = 9
# Output: [0,1]
print('Output:', Solution().twoSum(nums, target))


nums = [2,3,4]
target = 6
# Output: [1,2]

print('Output:', Solution().twoSum(nums, target))

nums = [-1, 0]
target = -1
# Output: [1,2]

print('Output:', Solution().twoSum(nums, target))

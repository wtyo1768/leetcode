


#HASH

class Solution:
    def twoSum(self, nums, target: int):

        k = {}
        for i in range(len(nums)):
            if nums[i] in k.keys():
                return [i, k[nums[i]]]
            else:
                k[target-nums[i]] = i






nums = [2,7,11,15]
target = 9
# Output: [0,1]
print('Output:', Solution().twoSum(nums, target))


nums = [3,2,4]
target = 6
# Output: [1,2]

print('Output:', Solution().twoSum(nums, target))

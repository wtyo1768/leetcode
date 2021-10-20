
class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1

        while(low<=high):
            mid = (high-low) // 2 + low

            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else: return mid
        return low


nums = [1,3,5,6]
target = 7
Output: 4
print('Output', Solution().searchInsert(nums, target))


nums = [1,3,5,6]
target = 0
Output: 0
print('Output', Solution().searchInsert(nums, target))


nums = [1]
target = 0
Output: 0
print('Output', Solution().searchInsert(nums, target))


nums = [1,3]
target = 2
Output: 1
print('Output', Solution().searchInsert(nums, target))

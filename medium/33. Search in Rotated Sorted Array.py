class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        start, end = 0, l-1

        # find bias
        while(start<end):
            mid = (start+end) // 2
            if nums[end]>nums[mid]:
                end = mid
            else:
                start = mid + 1

        # 偏移為最小值位置 - 0
        # find ans
        bias = start
        start, end = 0, l-1
        while(start < end):
            mid = (start+end) // 2
            real_mid = (mid+bias) % l

            value = nums[real_mid]
            if value>target:
                end = mid
            elif value<target:
                start = mid + 1
            else:
                return real_mid
        return -1


nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4
print('Output', Solution().search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
# Output: -1
print('Output', Solution().search(nums, target))

nums = [1]
target = 0
# Output: -1
print('Output', Solution().search(nums, target))

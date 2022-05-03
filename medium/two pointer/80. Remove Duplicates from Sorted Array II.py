

class Solution:
    def removeDuplicates(self, nums):
        
        lenth = len(nums)
        if lenth<=2: return nums
        x = 2

        for i in range(2, len(nums)):
            if nums[i] > nums[x-2]:
                nums[x] = nums[i]
                x += 1
        return x


nums = [1,1,1,2,2,3]
print('Output', Solution().removeDuplicates(nums), nums)
Output: 5 
# nums = [1,1,2,2,3,_]


nums = [0,0,1,1,1,1,2,3,3]
print('Output', Solution().removeDuplicates(nums), nums)
Output: 7 
# nums = [0,0,1,1,2,3,3,_,_]


nums = [1,1,1,2,3]
print('Output', Solution().removeDuplicates(nums), nums)
Output: 4
# nums = [1 1 2 3]

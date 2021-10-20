

class Solution:
    def search(self, nums, goal):
        head, tail = 0, len(nums)
        while(True):
            list_len = tail - head
            if list_len==1:
                if tail < len(nums) and nums[tail]==goal:
                    return tail
                if nums[head]==goal:
                    return head
                return -1
            mid = list_len // 2 + head
            if nums[mid] < goal:
                head = mid
            elif nums[mid] > goal:
                tail = mid
            else: return mid
        


nums = [-1,0,3,5,9,12]
target = 9
n = Solution().search(nums, target)
print('Output', n)
Output: 4

nums = [-1,0,3,5,9,12]
target = 2
n = Solution().search(nums, target)
print('Output', n)
Output: -1

nums = [5]
target = 5
n = Solution().search(nums, target)
print('Output', n)
Output: 0
# target = 1e9
# nums = [1556913,-259675,-7667451,-4380629,-4643857,-1436369,7695949,-4357992,-842512,-118463]
# n = Solution().search(nums, target)
# print(n)
# nums.insert(n, target)
# print('result',nums)
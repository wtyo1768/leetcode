

class Solution:
    def searchRange(self, nums, target: int):
        ans = []
        head, tail = 0, len(nums)-1

        while(head<=tail):
            # End of Search 
            if tail-head==1 or tail==head:
                if nums[head]==target:ans.append(head)
                if nums[tail]==target:ans.append(tail)
                if len(ans)==1: ans.append(ans[0])
                break

            mid = (head + tail) // 2
            # Found the target
            if nums[mid]==target:
                tmp = mid
                while(tmp-1>=0 and nums[tmp-1]==target):
                    tmp-=1
                ans.append(tmp)
                while(mid+1<=tail and nums[mid+1]==target):
                    mid+=1
                ans.append(mid)      
                break
            elif nums[mid]>target: tail = mid
            else: head = mid

        if len(ans)==0: return [-1, -1]
        return ans


nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]
print("Output", Solution().searchRange(nums, target))


nums = [5,7,7,8,8,10]
target = 6
# Output: [-1,-1]
print("Output", Solution().searchRange(nums, target))


nums = []
target = 0
# Output: [-1,-1]
print("Output", Solution().searchRange(nums, target))


nums = [1]
target = 0
# Output: [-1,-1]
print("Output", Solution().searchRange(nums, target))


nums = [1]
target = 1
# Output: [0, 0]
print("Output", Solution().searchRange(nums, target))


nums = [1, 1, 2]
target = 1
# Output: [0, 1]
print("Output", Solution().searchRange(nums, target))

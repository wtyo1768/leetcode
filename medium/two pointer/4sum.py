class Solution:
    def fourSum(self, nums, target: int):
        lenth = len(nums)-1
        if lenth<3: return []
        ans = []
        nums.sort()
        
        for left in range(lenth-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            
            for lmid in range(left+1, lenth-1):
                if lmid>left+1 and nums[lmid]==nums[lmid-1]:
                    continue

                rmid, right = lmid+1, lenth        
                t = target - nums[left] - nums[lmid]
                
                #early termination
                if 2*nums[rmid]>t: break
                while(rmid<right):
                    s = nums[rmid] + nums[right]
                    
                    if s<t:   rmid+=1
                    elif s>t: right-=1
                    else:
                        ans.append([nums[left], nums[lmid], nums[rmid], nums[right]])
                        while(rmid<right and nums[rmid]==nums[rmid+1]):
                            rmid+=1
                        while(rmid<right) and nums[right]==nums[right-1]:
                            right-=1
                        rmid+=1
                        right-=1
        return ans
                  
nums = [0,0,0,0]
target = 0
print('Output', Solution().fourSum(nums, target))
# Output: [[0,0,0,0]]


nums = [1,0,-1,0,-2,2]
target = 0
print('Output', Solution().fourSum(nums, target))
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums = [2,2,2,2,2]
target = 8
print('Output', Solution().fourSum(nums, target))
# Output: [[2,2,2,2]]

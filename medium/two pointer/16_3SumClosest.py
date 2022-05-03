



class Solution:
    def threeSumClosest(self, nums, target):
        ans=[]
        nums.sort()
        d = 10e6
        l = len(nums)
        for z in range(l-2):
            if z>0 and nums[z]==nums[z-1]: 
                continue
            i=z+1
            j=l-1
            curr_target = target - nums[z]
            while(i<j):
                s = nums[i]+nums[j]
                if abs(curr_target-s) < d:
                    d = abs(curr_target-s)
                    output = s + nums[z]
                
                if   s<curr_target:  i+=1
                elif s>curr_target:  j-=1
                else: return target
                    # ans.append([nums[i], nums[j], nums[z]])
                    # while(i<j and nums[i]==nums[i+1]):
                    #     i+=1
                    # while(i<j and nums[j]==nums[j-1]):
                    #     j-=1
                    # i+=1
                    # j-=1
        return output


nums = [-1,2,1,-4]
target = 1
# Output: 2
print('Output:', Solution().threeSumClosest(nums, target))

nums = [0,0,0]
target = 1
# Output: 0
print('Output:', Solution().threeSumClosest(nums, target))

nums = [1,1,1,0]
target = -100
# Output: 2
print('Output:', Solution().threeSumClosest(nums, target))


nums = [0,2,1,-3]
target = 1
# Output: 0
print('Output:', Solution().threeSumClosest(nums, target))

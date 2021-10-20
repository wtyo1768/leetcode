

# difficult

class Solution:
    def threeSum(self, nums):
        ans=[]
        nums.sort()
        l = len(nums)
        for z in range(l-2):
            if z>0 and nums[z]==nums[z-1]: 
                continue
            i=z+1
            j=l-1
            while(i<j):
                s = nums[i]+nums[j]
                
                if   s<-nums[z]:  i+=1
                elif s>-nums[z]:  j-=1
                else:
                    ans.append([nums[i], nums[j], nums[z]])
                    while(i<j and nums[i]==nums[i+1]):
                        i+=1
                    while(i<j and nums[j]==nums[j-1]):
                        j-=1
                    i+=1
                    j-=1

        return ans





nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print('Output:', Solution().threeSum(nums))


nums = [0]
# Output: []
print('Output:', Solution().threeSum(nums))


nums = []
print('Output:', Solution().threeSum(nums))

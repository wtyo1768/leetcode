

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

class Solution:
    def threeSum(self, nums):
        
        ans = []
        nums.sort()

        for i, t in enumerate(nums[:-2]):
            
            if i>0 and nums[i-1]==t: continue
            x, y = 0, len(nums)-1

            while(x<y):
                if x==i: x+=1
                if y==i: y-=1
                
                s = nums[x]+nums[y]
                
                if   s>-t: y-=1
                elif s<-t: x+=1
                else: 
                    ans.append([nums[i], nums[x], nums[y]])
                    while(x<y and nums[x]==nums[x+1]):
                        x+=1
                    while(x<y and nums[y]==nums[y-1]):
                        y-=1
                    x+=1
                    y-=1
        return ans



nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print('Output:', Solution().threeSum(nums))


nums = [0]
# Output: []
print('Output:', Solution().threeSum(nums))


nums = []
print('Output:', Solution().threeSum(nums))

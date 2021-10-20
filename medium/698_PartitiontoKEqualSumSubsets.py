
class Solution:
    def canPartitionKSubsets(self, nums, k) -> bool:
        
        target = sum(nums) / k 
        if not target.is_integer(): return False
        nums.sort(reverse=True)
        taken = [False] * len(nums)
         
        def can_parti(curr_k, start_idx=0, curr_sum=0):
            if curr_k==1: return True

            if curr_sum==target:
                return can_parti(curr_k-1)

            for i in range(start_idx, len(nums)):
                if not taken[i] and curr_sum+nums[i]<=target:
                    taken[i]=True       
                    if can_parti(curr_k, i+1, curr_sum+nums[i]):
                        return True
                    taken[i]=False
            return False
        return can_parti(k)




nums = [4,3,2,3,5,2,1]
k = 4   
# Output: true
print('Output :', Solution().canPartitionKSubsets(nums, k))


nums = [1,2,3,4]
k = 3
# Output: false  
print('Output :', Solution().canPartitionKSubsets(nums, k))

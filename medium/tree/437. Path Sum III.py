import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import *


class Solution:
    def dfs(self, root, curr_sum, targetSum, cache):
        if not root: return

        curr_sum = curr_sum + root.val
        old_pathsum = curr_sum - targetSum
        self.ans += cache.get(old_pathsum, 0)
        cache[curr_sum] = cache.get(curr_sum, 0) + 1
        
        if root.left:self.dfs(root.left, curr_sum, targetSum, cache)
        if root.right:self.dfs(root.right, curr_sum, targetSum, cache)
        ## Important
        cache[curr_sum] -= 1


    def pathSum(self, root, targetSum: int):
        self.ans = 0
        cache = {0:1}
        self.dfs(root, 0, targetSum, cache)
        
        return self.ans



root = [10,5,-3,3,2,None,11,3,-2,None,1]
targetSum = 8
# Output: 3
print('Output :', Solution().pathSum(build_tree(root), targetSum))


root =  [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
# Output: 3
print('Output :', Solution().pathSum(build_tree(root), targetSum))

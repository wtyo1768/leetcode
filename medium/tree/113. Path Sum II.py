import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import *


class Solution:
    def helper(self, root, path, target):
        if not root:
            return
        if root.left==None and root.right==None and root.val==target:
            self.ans.append(path+[root.val])
        
        self.helper(root.left, path+[root.val], target-root.val), \
        self.helper(root.right, path+[root.val], target-root.val)


    def pathSum(self, root, targetSum: int):
        self.ans = []
        self.helper(root, [], targetSum)

        return self.ans



root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
print('Output :', Solution().pathSum(build_tree(root), targetSum))



root = [1,2,3]
targetSum = 5
# Output: []
print('Output :', Solution().pathSum(build_tree(root), targetSum))



root = [1,2]
targetSum = 0
# Output: []
print('Output :', Solution().pathSum(build_tree(root), targetSum))
 
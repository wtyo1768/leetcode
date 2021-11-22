

import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import build_tree, TreeNode


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root: return 0

        if not root.left==None:
            if root.left.left==None and root.left.right==None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



root = [3,9,20, None, None, 15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
print('Output :', Solution().sumOfLeftLeaves(build_tree(root)))


root = [1]
# Output: 0
print('Output :', Solution().sumOfLeftLeaves(build_tree(root)))

root = [1,2,3,4,5]
# Output: 4
print('Output :', Solution().sumOfLeftLeaves(build_tree(root)))

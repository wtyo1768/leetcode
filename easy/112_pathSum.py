import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import build_tree, TreeNode


# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum):
#         if not root: return False
        
#         # Is leaf
#         if root.left==None and root.right==None:
#             if targetSum-root.val==0:return True
#             else: return False

#         if root.left and root.right:
#             return self.hasPathSum(root.left, targetSum-root.val) or  self.hasPathSum(root.right, targetSum-root.val)
#         elif root.left:
#             return self.hasPathSum(root.left, targetSum-root.val)
#         elif root.right:
#             return self.hasPathSum(root.right, targetSum-root.val)

## 優化
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum):
        if not root: return False
        
        # Is leaf
        if root.left==None and root.right==None:
            if targetSum-root.val==0:return True
            else: return False

        return self.hasPathSum(root.left, targetSum-root.val) or  self.hasPathSum(root.right, targetSum-root.val)
#        

## Web Sol
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
# Output: true


print('Output :', Solution().hasPathSum(build_tree(root), targetSum))

root = [1,2,3]
targetSum = 5
# Output: false
print('Output :', Solution().hasPathSum(build_tree(root), targetSum))

root = []
targetSum = 1
# Output: false
print('Output :', Solution().hasPathSum(build_tree(root), targetSum))


root = [1,2]
targetSum = 1
print('Output :', Solution().hasPathSum(build_tree(root), targetSum))

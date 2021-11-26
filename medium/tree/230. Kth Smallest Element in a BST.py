
import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import build_tree, TreeNode


#DFS
class Solution:
    def count_subtree_nums(self, root):
        if root:
            return 1+self.count_subtree_nums(root.left)+self.count_subtree_nums(root.right)
        else:
            return 0

    def kthSmallest(self, root, k: int) -> int:

        subtree_Nums = self.count_subtree_nums(root.left)
    
        if subtree_Nums>=k:
            return self.kthSmallest(root.left, k)
        elif subtree_Nums+1<k:
            return self.kthSmallest(root.right, k-1-subtree_Nums)
        return root.val


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        # print(count)
        return count[k-1]
        
    def helper(self, node, count):
        if not node: return
        
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)



root = [3,1,4,None,2]
k = 1
# Output: 1
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
print('Output :', Solution().kthSmallest(build_tree(root), k))


root = [5,3,6,2,4,None,None,1]
k = 3
# Output: 3
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
print('Output :', Solution().kthSmallest(build_tree(root), k))

        
root = [1]
k = 1
# Output: 1
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
print('Output :', Solution().kthSmallest(build_tree(root), k))


root = [1, None, 2]
k = 2
# Output: 1
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
print('Output :', Solution().kthSmallest(build_tree(root), k))

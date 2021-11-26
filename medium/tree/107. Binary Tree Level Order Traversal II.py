
import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import *


'''
First build a stack to represent the given tree structure

then pop each node of the stack to traverse the tree in the reverse form.
'''
class Solution(object):
    def levelOrderBottom(self, root):
        s, level = [], [0]
        tree_stack, ans = [], []
        level2 = [0]
        if root: s.append(root)

        while(not len(s)==0):
            root, l = s.pop(0), level.pop(0)
            
            tree_stack.append(root), level2.append(l)

            if root.right:
                s.append(root.right)
                level.append(l+1)
            if root.left:
                s.append(root.left)
                level.append(l+1)
            
        prev_l = None
        while(not len(tree_stack)==0):
            root, l = tree_stack.pop(), level2.pop()

            if not prev_l==l:
                ans.append([root.val])
            else:
                ans[-1].append(root.val)
            prev_l = l

        return ans


root = [3,9,20,None,None,15,7]
# Output: [[15,7],[9,20],[3]]
print(Solution().levelOrderBottom(build_tree(root)))



root = [1]
# Output: [[1]]
print(Solution().levelOrderBottom(build_tree(root)))



root = []
# Output: []
print(Solution().levelOrderBottom(build_tree(root)))

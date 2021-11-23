
import sys
sys.path.append('/home/rockyo/Desktop/leetcode')
from ds import *


class Solution(object):
    def levelOrder(self, root):
        ans, q = [], []
        level = [0]
        
        if root: q.append(root)
        while(not len(q)==0):
            root, l = q.pop(0), level.pop(0)
            
            if len(ans)<=l:
                ans.append([])
                ans[l].append(root.val)
            else:
                ans[l].append(root.val)
            
            if root.left:
                q.append(root.left)
                level.append(l+1)
            if root.right:
                q.append(root.right)
                level.append(l+1)
        return ans


root = [3,9,20,None,None,15,7]
# Output: [[3],[9,20],[15,7]]
print(Solution().levelOrder(build_tree(root)))



root = [1]
# Output: [[1]]
print(Solution().levelOrder(build_tree(root)))



root = []
# Output: []
print(Solution().levelOrder(build_tree(root)))

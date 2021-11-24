
import sys
sys.path.append('/home/rockyo/Desktop/leetcode')
from ds import *


# Web
class Solution(object):
    def zigzagLevelOrder(self, root):
        ans, q = [], []
        if root: q.append(root)
        zigzag = False
        
        while(not len(q)==0):    
            level_sz = len(q)
            level_output = []
                    
            for _ in range(0, level_sz):
                root = q.pop(0)
                if zigzag:
                    level_output.insert(0, root.val)
                else:
                    level_output.append(root.val)
                    
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                    
            zigzag = not zigzag
            ans.append(level_output)
        return ans


root =   [3,9,20,None,None,15,7]
# Output:  [[3],[20,9],[15,7]]
print(Solution().zigzagLevelOrder(build_tree(root)))

 

root = [1]
# Output: [[1]]
print(Solution().zigzagLevelOrder(build_tree(root)))



root = []
# Output: []
print(Solution().zigzagLevelOrder(build_tree(root)))

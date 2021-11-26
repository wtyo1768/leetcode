"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root: q = [root]
        else: q = []
        ans = []
        curr = None
        level = [0]
        
        while(not len(q)==0):
            curr, l = q.pop(0), level.pop(0)
            
            for c in curr.children:
                q.append(c)
                level.append(l+1)
            
            if len(ans)<=l: ans.append([curr.val])
            else: ans[l].append(curr.val)
            
        return ans
            
            
        
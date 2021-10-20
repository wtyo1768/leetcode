import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import build_tree


class RecursionSolution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))


### breadth-first-search, level order traversal
class Solution(object):
    def maxDepth(self, tree):
        if tree is None:return 0
        tree.h = 1
        ans = 0
        q = []
        q.append(tree)
        
        while(True):
            if len(q)==0:break
            n = q.pop(0)
            l = n.h
            ans = max(ans, l)
            if not n==None:
                if n.left : 
                    n.left.h = l+1
                    q.append(n.left)
                if n.right:
                    n.right.h = l+1
                    q.append(n.right)
                    
        return ans
#
import queue
def traverse(tree):
    q = queue.Queue()
    q.put(tree)
    while(True):
        if q.empty():break
        n = q.get()
        if n: print(n.val)
        else: print(None)
        if not n==None:
            q.put(n.left)
            q.put(n.right)

root = [3,9,20,None,None,15,7]
Output: 3

print('output:', Solution().maxDepth(build_tree(root)))
# tree = build_tree(root)
# traverse(tree)


root = [1,None,2]
Output: 2
print('output:', Solution().maxDepth(build_tree(root)))




root = []
Output: 0
print('output:', Solution().maxDepth(build_tree(root)))


root = [0]
Output: 1
print('output:', Solution().maxDepth(build_tree(root)))

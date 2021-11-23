import sys
sys.path.append('/home/rockyo/Desktop/leetcode')
from ds import build_tree, TreeNode



class Solution:
    def inorderTraversal(self, root: TreeNode):
        ans = []
        curr = root
        s = []
        while(len(s)!=0 or not curr==None):
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                n = s.pop()
                ans.append(n.val)
                curr = n.right
        return  ans


    def preorderTraversal(self, root: TreeNode):
        ans = []
        curr = root
        s = []
        while(not len(s)==0 or not curr==None):
            if curr:
                s.append(curr)
                ans.append(curr.val)
                curr = curr.left
            else:
                n = s.pop()
                curr = n.right
        return ans


    def postorderTraversal(self, root: TreeNode):
        ans = []
        s = [root]
        if root==None:
            return []
        while(len(s)):
            curr = s[-1]
            if not curr.left and not curr.right:
                s.pop()
                ans += [curr.val]
            
            if curr.right:
                s+=[curr.right]
                curr.right = None
            
            if curr.left:
                s+=[curr.left]
                curr.left = None
        return ans



root = [3,1,2]
Output= [1, 3, 2]

print(Solution().postorderTraversal(build_tree(root)))

root = []
Output = []
print(Solution().postorderTraversal(build_tree(root)))


root = [1]
Output = [1]
print(Solution().postorderTraversal(build_tree(root)))


root = [1, 2]
Output = [2, 1]
print(Solution().postorderTraversal(build_tree(root)))


root = [1, None, 2]
Output = [1, 2]
print(Solution().postorderTraversal(build_tree(root)))

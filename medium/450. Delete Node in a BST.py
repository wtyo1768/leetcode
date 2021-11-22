import sys
sys.path.append('/home/rockyo/Desktop/leetcode')
from ds import build_tree, TreeNode


class Solution:
    def deleteRootNode(self, root):

        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            min_node = root.right
            while(True):
                if min_node.left: min_node = min_node.left
                else: break
            # origin_left = root.left
            
            min_node.left = root.left
            
            return root.right
    
                
    def deleteNode(self, root, key: int):
        curr = root
        if root and root.val==key:
            return None
        prev = curr
        while(not curr==None and not curr.val==key):
            prev = curr
            if curr.val<key: curr = curr.right
            else: curr = curr.left
            
        if curr==None: return root
        
        if prev.left == curr:
            prev.left = self.deleteRootNode(curr)
        else:
            prev.right = self.deleteRootNode(curr)
        
        return root

    

root = [5,3,6,2,4,None,7]
key = 3
# Output: [5,4,6,2,None,None,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,None,None,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,None,4,None,7] and it's also accepted.
print(Solution().deleteNode(build_tree(root), key))


root = [5,3,6,2,4,None,7]
key = 0
# Output: [5,3,6,2,4,None,7]
# Explanation: The tree does not contain a node with value = 0.
print(Solution().deleteNode(build_tree(root), key))


root = []
key = 0
# Output: []
print(Solution().deleteNode(build_tree(root), key))


root = [0]
key = 0
# Output: []
print(Solution().deleteNode(build_tree(root), key))
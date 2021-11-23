import sys
sys.path.append('/home/rockyo/Desktop/leetcode')
from ds import *

class Solution:
    def deleteRootNode(self, root):

        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            min_node = root.right
            prev_node = root
            while(True):
                if min_node.left: 
                    prev_node = min_node
                    min_node = min_node.left
                else: break
            
            # min node did'nt have left child 
            if prev_node.left==min_node:
                prev_node.left = min_node.right
            elif prev_node.right==min_node:
                prev_node.right = min_node.right
                
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
            return root
    
                
    def deleteNode(self, root, key: int):
        curr = root
        prev = curr
        while(not curr==None and not curr.val==key):
            prev = curr
            if curr.val<key: curr = curr.right
            else: curr = curr.left
            
        # key not found in the tree
        if curr==None: return root
        
        if curr==prev: return self.deleteRootNode(curr)
        
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
printTree(Solution().deleteNode(build_tree(root), key))


root = [5,3,6,2,4,None,7]
key = 0
# Output: [5,3,6,2,4,None,7]
# Explanation: The tree does not contain a node with value = 0.
printTree(Solution().deleteNode(build_tree(root), key))


root = []
key = 0
# Output: []
printTree(Solution().deleteNode(build_tree(root), key))


root = [0]
key = 0
# Output: []
printTree(Solution().deleteNode(build_tree(root), key))


root = [5,3,6,2,4,None,7]
key = 5
# Output: [6,3,7,2,4]
printTree(Solution().deleteNode(build_tree(root), key))


root = [50,30,70,None,40,60,80]
key = 50
# Output: [60,30,70,null,40,null,80]
printTree(Solution().deleteNode(build_tree(root), key))
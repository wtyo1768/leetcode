# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(root):
    q = []
    tree = TreeNode(root[0]) if len(root) != 0 else None
    q.append(tree)
    i = 1
    while True:
        n = q.pop(0)
        if n==None:
            if len(q)==0: break
            continue
        if i>len(root)-1:
            break
        n.left = TreeNode(root[i]) if root[i]!= None else None 
        q.append(n.left)

        if i+1>len(root)-1:
            break
        n.right = TreeNode(root[i+1]) if root[i+1] != None else None 
        q.append(n.right)
        i+=2
    return tree


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(arr):
    if len(arr)==0:
        return None
    l = ListNode(arr[0])
    begin = l
    for e in arr[1:]:
        subl  = ListNode(e)
        l.next = subl
        l = subl
    return begin

def printList(l):
    print('--------')
    ans = []
    while(True):
        if l==None:break
        ans.append(l.val)
        l = l.next
    print(ans)
    
    
def printTree(root):
    queue = [root]
    curr = None
    output = []
    while(curr or not len(queue)==0):
        curr = queue.pop(0)
        if curr: 
            output.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else: output.append(None)

    while(not len(output)==0 and output[-1]==None): output.pop()
    print(output)
    
# printTree(build_tree([1,2,3]))
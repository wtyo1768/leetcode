
import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList



class Solution:
    def removeNthFromEnd(self, head, n):
        l = 0
        curr = head
        while(curr):
            curr=curr.next
            l+=1
        del_idx = l-n

        curr = head
        while(del_idx>1):
            curr=curr.next
            del_idx-=1

        if del_idx==0:
            head=head.next
        else:
            curr.next = curr.next.next
        
        return head

# Single pass sol (WEB)
class Solution:
    def removeNthFromEnd(self, head, n):
        i, j = head, head
        for _ in range(n):
            j=j.next
        
        if j==None:
            return i.next
        
        while(j.next!=None):
            i=i.next
            j=j.next
        i.next=i.next.next

        return head

head = [1,2,3,4,5]
n = 2
# Output: [1,2,3,5]
l = Solution().removeNthFromEnd(createList(head), n)
printList(l)


head = [1] 
n = 1
# Output: []
l = Solution().removeNthFromEnd(createList(head), n)
printList(l)


head = [1,2] 
n = 1
# Output: [1]
l = Solution().removeNthFromEnd(createList(head), n)
printList(l)


head = [2,1] 
n = 2
# Output: [1]
l = Solution().removeNthFromEnd(createList(head), n)
printList(l)
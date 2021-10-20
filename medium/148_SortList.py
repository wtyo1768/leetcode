import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList


class Solution:
    
    def merge(self, l, r):
        head = ListNode(None)
        begin = head
        while(l and r):
            if l.val < r.val:
                head.next = l
                head, l = head.next, l.next
            else:
                head.next = r
                head, r = head.next, r.next
        head.next = l or r
        return begin.next

    def sortList(self, head):        
        if head==None or head.next==None:
            return head
        slow, fast = head, head.next
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next

        fast = slow.next
        slow.next = None    
        l, r = self.sortList(head), self.sortList(fast)
        return self.merge(l, r)






head = [4,2,1,3]
# Output: [1,2,3,4]
printList(Solution().sortList(createList(head)))


head =  [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
printList(Solution().sortList(createList(head)))

head =  []
# Output: []
printList(Solution().sortList(createList(head)))

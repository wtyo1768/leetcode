import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None: return None

        if head.next: l=head.next
        else: l = head

        while head and head.next:
            next_node = head.next.next

            head.next.next = head

            if next_node and next_node.next:
                head.next = next_node.next
            else: head.next = next_node

            head = next_node
        return l


head = [1,2,3,4]
# Output: [2,1,4,3]

l = Solution().swapPairs(createList(head))
printList(l)

head = []
# Output: []
l = Solution().swapPairs(createList(head))
printList(l)


head = [1]
# Output: [1]
l = Solution().swapPairs(createList(head))
printList(l)



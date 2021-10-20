import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList




class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:   
        list_len = 0
        curr = head
        
        while(curr):
            curr=curr.next
            list_len+=1

        begin=head
        if list_len>=k:
            for _ in range(k-1):
                begin=begin.next

        curr = head
        for i in range(list_len // k):
            group_tail = curr
            pre_node = curr
            curr = curr.next

            for _ in range(k-1):
                # 存原本node的next
                next_node = curr.next
                # 改變node連接方向
                curr.next = pre_node
                pre_node = curr
                curr = next_node

            if i==(list_len // k)-1:
                group_tail.next = curr
            else:
                n = curr
                for _ in range(k-1):
                    n=n.next
                group_tail.next = n
            
        return begin



head = [1,2,3,4,5]
k = 5
l = Solution().reverseKGroup(createList(head), k)
printList(l)


head = [1,2,3,4,5]
k = 3
l = Solution().reverseKGroup(createList(head), k)
printList(l)



head = [1,2,3,4,5]
k = 2
l = Solution().reverseKGroup(createList(head), k)
printList(l)


head = [1,2,3,4,5]
k = 1
l = Solution().reverseKGroup(createList(head), k)
printList(l)
# Output: [1,2,3,4,5]

head = [1]
k = 1
l = Solution().reverseKGroup(createList(head), k)
printList(l)
# Output: [1]
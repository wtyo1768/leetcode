import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList

# 57.63% speed, 20.82% memory
class Naive_Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
            list_length = 0
            s = head
            while(s):
                list_length+=1
                s=s.next
            
            l=head
            curr_pos = 1
            # print(list_length-k+1, list_length)
            while(head):
                if curr_pos==k:
                    first=head
                if curr_pos==list_length-k+1:
                    last=head
                head = head.next
                curr_pos+=1
            first.val, last.val = last.val, first.val
            return l

#speed 5%, 95.22 memory
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
            tmp = []
            
            l=head
            curr_pos = 1
            while(head):
                if curr_pos==k:
                    first=head
                if len(tmp)==k:
                    tmp.pop(0)    
                tmp.append(head)
                head = head.next
                curr_pos+=1

            last=tmp[0]
            first.val, last.val = last.val, first.val
            return l


head = [1,2,3,4,5]
k = 2
# [1,4,3,2,5]
l = Solution().swapNodes(createList(head), k)
printList(l)



head = [7,9,6,6,7,8,3,0,9,5]
k = 5
# [7,9,6,6,8,7,3,0,9,5]
l = Solution().swapNodes(createList(head), k)
printList(l)

head = [1]
k = 1
# Output: [1]
l = Solution().swapNodes(createList(head), k)
printList(l)

head = [1,2]
k = 1
# Output: [2,1]
l = Solution().swapNodes(createList(head), k)
printList(l)


head = [1,2,3]
k = 2
# Output: [1,2,3]
l = Solution().swapNodes(createList(head), k)
printList(l)

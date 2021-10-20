import sys
sys.path.append('C:\\Users\\rockyo\\Desktop\\leetcode')
from ds import ListNode, createList, printList


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        o = ListNode()
        s = o
        while True:
            if l1==None and l2==None:
                if not carry ==0: 
                    val=0
                else:break
            elif l1==None: val=l2.val
            elif l2==None: val=l1.val
            else:          val = l1.val + l2.val

            sum   = (val+carry)
            val   = sum%10
            carry = sum// 10

            node = ListNode(val)
            if l1: l1=l1.next
            if l2: l2=l2.next

            o.next = node
            o = node
        return s.next


arr1 = [2,4,3]
arr2 = [5,6,4]
arr1 = [9,9,9,9,9,9,9]
arr2 = [9,9,9,9]

l = Solution().addTwoNumbers(createList(arr1), createList(arr2))
printList(l)


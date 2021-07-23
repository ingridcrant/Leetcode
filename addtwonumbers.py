# python implementation of add two numbers problem on leetcode

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def constructLinkedList(self, reverseddigits, digitplace):
        if digitplace == len(reverseddigits)-1:
            return ListNode(reverseddigits[digitplace])
        else:
            return ListNode(reverseddigits[digitplace], self.constructLinkedList(reverseddigits, digitplace+1))
    
# l1 -> ListNode
# l2 -> ListNode
def addTwoNumbers(l1, l2):
    digits = []
    carryover = 0
    endofl1 = False
    endofl2 = False
    
    while not endofl1 or not endofl2:
        if not endofl1 and not endofl2:
            new_sum = l1.val + l2.val + carryover
        elif not endofl1 and endofl2:
            new_sum = l1.val + carryover
        elif endofl1 and not endofl2:
            new_sum = l2.val + carryover
        digits.append(new_sum % 10)
        carryover = new_sum // 10
        
        if l1.next != None:
            l1 = l1.next
        else:
            endofl1 = True
        
        if l2.next != None:
            l2 = l2.next
        else:
            endofl2 = True
    
    if carryover > 0:
        digits.append(carryover)
    
    l = ListNode()
    return l.constructLinkedList(digits, 0)

# test case
l = ListNode()
l1 = l.constructLinkedList([2, 4 ,3], 0)
l2 = l.constructLinkedList([5, 6 ,4], 0)
print(addTwoNumbers(l1, l2))
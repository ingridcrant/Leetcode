# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    attachment = None
    came_back_to_head = False
    
    def find_nth_from_last(self, node, n):
        if node.next == None:
            return 1
        else:
            from_last = self.find_nth_from_last(node.next, n) + 1
            if from_last == n:
                self.attachment = node.next
            elif from_last == n + 1:
                node.next = self.attachment
                self.came_back_to_head = True
                
            return from_last
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        throwaway = self.find_nth_from_last(head, n)
        if not self.came_back_to_head:
            return self.attachment
        else:
            return head
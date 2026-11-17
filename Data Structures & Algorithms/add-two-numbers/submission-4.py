# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            n = l1.val + l2.val
            
            if n >= 10:
                carry = n % 10
                other = n // 10
                curr.next = ListNode(carry)
                curr = curr.next

                curr.next = ListNode(other)
                curr = curr.next
            
            else:
                curr.next = ListNode(n)
                curr = curr.next

            l1 = l1.next
            l2 = l2.next
            if l2 is None:
                l2 = 0
            if l1 is None:
                l1 = 0

        
        return dummy.next
        
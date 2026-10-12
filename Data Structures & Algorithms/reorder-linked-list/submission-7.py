# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        res = []
        curr = head
        
        while curr:
            res.append(curr)
            curr = curr.next

        l, r = 0, len(res) - 1
        while l < r:
            res[l].next = res[r]
            l += 1
            if l >= r:
                break
            res[r].next = res[l]
            r-=1
        
        res[l].next = None

        
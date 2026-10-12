class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Store the second half in an array
        second = []
        curr = slow.next
        slow.next = None

        while curr:
            second.append(curr)
            curr = curr.next

        # Merge using the array backwards
        curr = head
        while second:
            node = second.pop()
            node.next = curr.next
            curr.next = node
            curr = node.next
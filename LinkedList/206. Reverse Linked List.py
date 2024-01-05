class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        if head.next is None:
            return head

        temp = head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
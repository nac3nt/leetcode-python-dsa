class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        _list = []

        while head is not None:
            _list.append(head.val)
            head = head.next

        while left < right:
            _list[left - 1], _list[right - 1] = _list[right - 1], _list[left - 1]
            left += 1
            right -= 1

        temp = head = ListNode()
        for x in _list:
            temp.next = ListNode(x)
            temp = temp.next

        return head.next

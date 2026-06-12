class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort left and right halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted lists
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next
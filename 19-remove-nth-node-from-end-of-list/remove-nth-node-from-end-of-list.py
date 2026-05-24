class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # fast ko n+1 step aage le jao
        for i in range(n + 1):
            fast = fast.next

        # dono pointer move karo
        while fast:
            fast = fast.next
            slow = slow.next

        # node delete karo
        slow.next = slow.next.next

        return dummy.next
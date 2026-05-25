# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dummy  = ListNode(0)
        dummy.next = head
        slow =dummy
        fast =head 

        while fast and fast != slow :
            fast = fast.next
            if fast :
                fast = fast.next
            slow = slow.next

        return fast != None
        
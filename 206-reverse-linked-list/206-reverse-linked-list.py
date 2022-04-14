# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        n = head
        while n:
            nextnode = n.next
            n.next = prev
            prev = n
            n = nextnode
        return prev
        
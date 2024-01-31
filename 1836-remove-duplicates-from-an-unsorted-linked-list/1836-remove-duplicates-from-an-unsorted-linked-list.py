# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        values = set()
        duplicates = set()
        current = head
        while current:
            if current.val in values:
                duplicates.add(current.val)
            else:
                values.add(current.val)
            current = current.next
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        while current:
            if current.val in duplicates:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next
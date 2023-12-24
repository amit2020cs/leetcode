# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ls.sort()
        s=t=ListNode()
        for i in ls:
            s.next = ListNode(i)
            s=s.next
        return t.next
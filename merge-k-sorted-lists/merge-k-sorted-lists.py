# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
            a.sort()
        s=t=ListNode()
        for i in a:
            s.next = ListNode(i)
            s=s.next
        return t.next
        

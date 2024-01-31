# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
            
        res[k - 1], res[-k] = res[-k], res[k - 1]
        
        head1 = ListNode(res[0])
        current = head1

        # Iterate through the array to create the linked list
        for element in res[1:]:
            current.next = ListNode(element)
            current = current.next

        return head1
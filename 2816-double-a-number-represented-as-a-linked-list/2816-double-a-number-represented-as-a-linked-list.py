# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        num = []
        
        while head:
            num.append(head.val)
            head = head.next
        
        carry = 0
        res = []
        while num:
            carry += num.pop()*2
            res.append(carry%10)
            carry //= 10
        if carry:
            res.append(carry)
        res.reverse()
        head = None
        while res:
            head = ListNode(res.pop(), head)
        return head
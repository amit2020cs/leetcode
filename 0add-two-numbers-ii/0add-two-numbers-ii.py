# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = []
        num2 = []
        
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        res = []
        carry = 0
        while num1 or num2:
            if num1:
                carry += num1.pop()
            if num2:
                carry+= num2.pop()
                
            res.append(carry%10)
            carry//=10
        if carry:
            res.append(carry)
        res.reverse()
        
        head = None
        while res:
            head = ListNode(res.pop(),head)
        return head
            
            
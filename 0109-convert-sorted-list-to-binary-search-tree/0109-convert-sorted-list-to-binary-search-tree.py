# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMid(self, head):
        prevptr = None
        slowptr = head
        fastptr = head
        
        while fastptr and fastptr.next:
            prevptr = slowptr
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        
        if prevptr:
            prevptr.next = None
        return slowptr
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        
        mid = self.findMid(head)
        
        node = TreeNode(mid.val)
        
        if head == mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
        
        
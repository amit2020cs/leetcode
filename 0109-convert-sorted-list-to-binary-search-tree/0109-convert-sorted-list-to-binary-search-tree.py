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
    
    def maptolist(self, head):
        value = []
        
        while head:
            value.append(head.val)
            head = head.next
        
        return value
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = self.maptolist(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l, r):

            # Invalid case
            if l > r:
                return None

            # Middle element forms the root.
            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if l == r:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node
        return convertListToBST(0, len(values) - 1)
            
#         if not head:
#             return None
        
#         mid = self.findMid(head)
        
#         node = TreeNode(mid.val)
        
#         if head == mid:
#             return node
        
#         node.left = self.sortedListToBST(head)
#         node.right = self.sortedListToBST(mid.next)
        
#         return node
        
        
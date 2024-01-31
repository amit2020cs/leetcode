# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, x,y) -> 'PolyNode':
        head = cur = PolyNode(-1, -1)
        while x and y:
            nex = None
            if x.power==y.power:
                if x.coefficient+y.coefficient:
                    nex = PolyNode(x.coefficient+y.coefficient, x.power)
                x = x.next
                y = y.next
            elif x.power>y.power:
                nex = PolyNode(x.coefficient, x.power)
                x = x.next
            else:
                nex = PolyNode(y.coefficient, y.power)
                y = y.next
            if nex:
                cur.next = nex
                cur = nex
        while x:
            nex = PolyNode(x.coefficient, x.power)
            x = x.next
            cur.next = nex
            cur = nex
        while y:
            nex = PolyNode(y.coefficient, y.power)
            y = y.next
            cur.next = nex
            cur = nex
        return head.next
        
        
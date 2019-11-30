# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = new = ListNode(None)
        if l1 == None:
            return l2
        if l2 == None:
            return l1 
        while l1 and l2:
            if l1.val == l2.val:
                new.next = ListNode(l1.val)
                new = new.next
                new.next = ListNode(l2.val)
                new = new.next
                l1 = l1.next
                l2 = l2.next
            elif l1.val < l2.val:
                new.next = ListNode(l1.val)
                new = new.next
                l1 = l1.next
            elif l1.val > l2.val:
                new.next = ListNode(l2.val)
                new = new.next
                l2 = l2.next
        if l1!=None:
            while l1:
                new.next = ListNode(l1.val)
                new = new.next
                l1 = l1.next
        if l2!=None:
            while l2:
                new.next = ListNode(l2.val)
                new = new.next
                l2 = l2.next
        return root.next
                
            

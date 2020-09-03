# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l = ListNode()
        summ = 0
        while l1!=None or l2!=None:
            
            summ//=10
            if l1!=None:
                summ +=l1.val
                l1 = l1.next
            
            if l2!=None:
                summ +=l2.val
                l2 = l2.next
                
            l.next = ListNode(summ%10)
            l = l.next
        
        if summ//10 == 1:
            l.next = ListNode(1)
        return head.next
    
            
       

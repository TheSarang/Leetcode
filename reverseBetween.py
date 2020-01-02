# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        cur = head
        top = cur.next
        count = 1
        while count < m:
            pre = cur
            cur = top
            top = top.next
            count+=1
                
        bottom = pre
        bottomNext = cur
        while count < n:
            pre = cur
            cur = top
            top = top.next
            cur.next = pre
            count+=1
                
        bottomNext.next = top
        if m == 1:
            return cur
        bottom.next = cur
        
        return head

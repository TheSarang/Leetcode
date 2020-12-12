# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = post = dummy
        
        for _ in range(n):
            post = post.next
            
        while post and post.next:
            pre = pre.next
            post = post.next
            
        pre.next = pre.next.next
        return dummy.next
        

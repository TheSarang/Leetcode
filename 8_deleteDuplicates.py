# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev = head
        cur = prev.next
        while cur != None:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        return head

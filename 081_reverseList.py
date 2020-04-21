# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        self.top = None
        while cur != None:
            self.top = cur.next
            cur.next = prev
            prev = cur
            cur = self.top
        head = prev

        return head

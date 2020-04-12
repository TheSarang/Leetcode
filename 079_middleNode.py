# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def getSize():
            size = 0
            cur = head
            while cur != None:
                size += 1
                cur = cur.next
            return size
        
        mid = getSize() // 2
        cur = head
        target = 0
        while cur != None and target < mid:
            cur = cur.next
            target +=1
        head = cur
        return head
        
        #-----------------------------------------
 class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head

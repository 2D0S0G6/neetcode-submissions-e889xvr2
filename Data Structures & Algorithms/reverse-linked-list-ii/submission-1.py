# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right :
            return head
        if left == 1 :
            prev = None
            curr = head

            for i in range(right):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head.next = curr
            return prev
        left_prev = head
        for i in range(left-2):
            left_prev = left_prev.next
        left_node = left_prev.next
        prev = None
        curr = left_node
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        left_prev.next = prev
        left_node.next = curr
        
        return head
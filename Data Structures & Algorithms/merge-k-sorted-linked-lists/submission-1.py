# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = mergeTwoLists(list1.next,list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1,list2.next)
                return list2
        if not lists:
            return None
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
        
        return lists[-1]
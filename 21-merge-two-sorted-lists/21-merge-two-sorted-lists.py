# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = list3 = ListNode()          #creating new list to store and pointer to it
        while list1 and list2:              
            if list1.val < list2.val:       #if list1.val is small add that list3 
                list3.next = list1
                list1 = list1.next
            else:                           #if list2.val is small add that list3 
                list3.next = list2
                list2 = list2.next
            list3 = list3.next              #common increment of list3,instead of writing 2 times
        list3.next = list1 or list2         #if any list is till not empty
        return dummy.next
            
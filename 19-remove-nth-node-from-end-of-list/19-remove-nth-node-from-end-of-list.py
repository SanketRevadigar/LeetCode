# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point = head                                    #pointer at head and length variable
        length=0
        while point:                                    #to get the length of list
            point,length = point.next,length+1
            
        if length == n:                                 #if length = n remove  that element(first element)
            return head.next
        
        point = head                                    #as point is at last node, initialse again at head
        
        for i in range(1,length-n):                     #move till nth node to delete
            point = point.next
        point.next = point.next.next                    #remove the link
        
        return head                                     #return lit from beginning
            
        #Time complexity : O(L).The algorithm makes two traversal of the list, first to calculate list length L and             second to find the (L−n)th node. There are 2L−n operations and time complexity is O(L).

        #Space complexity : O(1).We only used constant extra space. 
        
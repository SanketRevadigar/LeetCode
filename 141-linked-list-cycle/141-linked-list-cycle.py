# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:                                   #if only 1 element
            return False
           
        slow = head                                         #use 2 pointer slow=1st node and fast=2nd node
        fast = head.next                                    #increment slow by 1 & fast by 2 everytime
        
        while slow!=fast:                                   #till both pointers have not met
            if not fast or not fast.next:                   #as fast moves 2 steps check if it goes out of bounds
                return False
            slow = slow.next
            fast = fast.next.next
           
        return (slow == fast)
        
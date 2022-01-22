# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        
        while fast and fast.next:                   #getting the middle node,as slow will be at middle, if fast goes out
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next                          #separting the second half
        prev = slow.next = None
        
        while second:                               #reversing the second half
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first,second = head,prev
        while second:                               #merging 2nd half into 1st half
            temp1,temp2 = first.next,second.next    #storing next values to iterate forward
            first.next = second
            second.next = temp1
            first = temp1
            second=temp2
        
        #Time complexity: O(N). There are three steps here. To identify the middle node takes O(N) time. To reverse the         second part of the list, one needs N/2 operations. The final step, to merge two lists, requires N/2operations as         well. In total, that results in O(N) time complexity.

        #Space complexity: O(1), since we do not allocate any additional data structures.

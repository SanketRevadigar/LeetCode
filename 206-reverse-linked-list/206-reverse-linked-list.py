# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None                       #empty pointer
        temp = head                       #set a pointer to first node
        
        while temp:                     
            nxt = temp.next               #before breaking link store in nxt variable
            temp.next = prev              #break the link and link to new empty prev node
            prev = temp                   #now change prev node to 1st node
            temp = nxt                    #and move the 1st node pointer to 2nd node
        return prev                       #prev will be at end so return prev
        
        
        #Time complexity : O(n). Assume that nnn is the list's length, the time complexity is O(n).

        #Space complexity : O(1).

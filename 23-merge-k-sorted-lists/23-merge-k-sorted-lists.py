# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        # initialize heap
        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        # initialize nodelist to return
        head = ListNode()
        node = head
		# merge
        while heap:
            # pop the min from heap
            value, i = heapq.heappop(heap)
            # add node to output chain
            node.next = ListNode(value)
            node = node.next
            # move the pointer to the next node if there is one
            if lists[i].next:
                lists[i] = lists[i].next
                new_value = lists[i].val
				# push next element into the heap
                heapq.heappush(heap, (new_value, i))
        return head.next
        
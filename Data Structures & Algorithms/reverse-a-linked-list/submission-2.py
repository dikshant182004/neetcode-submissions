# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr =None, head
        # while curr:
        #     nxt=curr.next # temp var for next node loc
        #     curr.next=prev
        #     prev=curr
        #     curr=nxt
        # return prev

        # recursive solution 

        if not head:
            return None # check that whether the ll is empty or not 
        
        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head  # 4.next=5 -> 5.next=4
        head.next=None #4.next =None -> None<-4<-5

        return newHead


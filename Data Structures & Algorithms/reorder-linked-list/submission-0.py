class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find second half 
        slow,fast =head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half as we will be iterating to both the ll 
        second = slow.next 
        prev = slow.next =None 
        while second:
            tmp= second.next
            second.next=prev
            prev=second
            second =tmp 

        # merge two halfs 
        first_hf, second_hf = head, prev
        while second_hf:
            tmp1,tmp2= first_hf.next, second_hf.next
            first_hf.next = second_hf
            second_hf.next = tmp1
            first_hf, second_hf= tmp1,tmp2

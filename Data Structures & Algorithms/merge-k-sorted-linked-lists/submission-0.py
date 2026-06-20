
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force
        val =[]
        for i in lists:
            while i :
                val.append(i.val)
                i = i.next

        val.sort()

        dummy=ListNode(0)
        cur =dummy
        for i in val:
            cur.next=ListNode(i)
            cur=cur.next

        return dummy.next

        
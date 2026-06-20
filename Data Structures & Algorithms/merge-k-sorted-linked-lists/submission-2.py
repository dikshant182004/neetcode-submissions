
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # optimal one 
        if not lists and len(lists)==0:
            return None 

        # while len(lists)>1:
        #     merge_lst=[]
        #     for i in range(0,len(lists),2):
        #         l1=lists[i]
        #         l2=lists[i+1] if i+1 < len(lists) else None 
        #         merge_lst.append(self.merge(l1, l2))
        #     lists=merge_lst
        # return lists[0]

        for i in range(1,len(lists)):
            lists[i]=self.merge(lists[i-1],lists[i])
            
        return lists[-1]

    def merge(self, l1, l2):
        dummy =ListNode()
        tail = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1=l1.next 
            else:
                tail.next = l2 
                l2 = l2.next 
            tail=tail.next 

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2 
        return dummy.next 
        
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # do binary search to k =1 .... max (piles) 
        # no of piles < h 
        p1 , p2 = 1, max(piles)
        res = p2
        
        while p1<=p2:
            k= (p1 + p2)//2
            hours =0
            for i in piles :
                hours += math.ceil(i/k)
            
            if hours <= h:
                res = min(res , k)
                p2 = k-1
            else:
                p1 = k+1

        return res

    

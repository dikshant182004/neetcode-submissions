class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={} # hm for storing freqn of element
        p1=max_len=maxf=0

        for p2 in range(len(s)):
            count[s[p2]] = 1+ count.get(s[p2],0)
            # storing the max f so that we don't need to see the hm every time using 
            # using max(count.values()) for most freqn element at given time
            # we don't decrease it while moving the left ptr as it stores the most freq element at any given time
            maxf=max(maxf,count[s[p2]]) 
            while (p2-p1+1)-maxf > k:
                count[s[p1]] -=1
                p1+=1
            
            max_len=max(max_len,p2-p1+1)
        return max_len
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": return ""
        window,pane={},{}
        # window is big str and pane is the str to look for 
        for i in t:
            pane[i] = 1+ pane.get(i,0)

        have,need =0,len(pane)
        res, res_len = [-1,-1], math.inf
        p1=0
        for p2 in range(len(s)):
            c=s[p2]
            window[c] = 1+ window.get(c,0)

            if c in pane and window[c]==pane[c]:
                have +=1

            while have == need:
                if (p2-p1+1) < res_len:
                    res=[p1,p2]
                    res_len=(p2-p1+1)

                window[s[p1]] -=1 # squeezing 
                if s[p1] in pane and window[s[p1]] < pane[s[p1]]:
                    have -=1

                p1+=1

        l,r =res
        return s[l:r+1] if res_len != math.inf else ""    
        

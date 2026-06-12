class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains=set()
        p1=0
        max_len=0
        for p2, l in enumerate(s):
            while l in contains:   # abcabcbb
                contains.remove(s[p1]) # becz we don'e wanna count duplicate sub strings 
                p1+=1
            contains.add(l)
            max_len= max(max_len,p2-p1+1) 
        return max_len
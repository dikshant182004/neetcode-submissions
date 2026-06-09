class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        # since str can contain ascii character so encoding with a delimiter 
        # is not safe 
        for i in strs:
            s += str(len(i)) +"#"+ i
        return s

    def decode(self, s: str) -> List[str]:
        ans =[]
        p1=0
        while(p1<len(s)):
            p2=p1
            while(s[p2] != "#"):
                p2 +=1
            length = int(s[p1:p2])
            word = s[p2+1 : p2+1+length]
            ans.append(word)
            p1=p2+1+length
        return ans 
                

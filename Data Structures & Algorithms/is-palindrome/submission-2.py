class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=""
        for i in s :
            # if i.isalnum():
            if self.isalpha(i):
                s2 += i.lower()

        p1,p2=0,len(s2)-1
        while(p1<p2):
            if s2[p1] != s2[p2]: 
                return False
            p1 +=1
            p2 -=1
        return True 


    def isalpha(self,w):
        return (ord('A')<= ord(w)<= ord('Z') or
        ord('a')<= ord(w)<= ord('z') or 
        ord('0')<= ord(w)<= ord('9')) 

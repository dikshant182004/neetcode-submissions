class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_dict = Counter(s)
        if len(s) != len(t):
            return False
        for i in t: 
            if i not in map_dict or map_dict[i]==0:
                return False
            map_dict[i] -= 1
        return True 
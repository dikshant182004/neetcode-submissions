class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict=collections.defaultdict(list)
        for i in strs :
            key= str(sorted(list(i)))
            map_dict[key].append(i)
        return list(map_dict.values())
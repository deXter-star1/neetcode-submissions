from collections import defaultdict
strs=["act","pots","tops","cat","stop","hat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            dic["".join(sorted(word))].append(word)
        return list(dic.values())    
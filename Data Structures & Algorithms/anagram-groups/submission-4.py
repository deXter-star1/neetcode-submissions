from collections import defaultdict

strs=["act","pots","tops","cat","stop","hat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0] * 26
            for char in word:
                lst[ord(char) - ord('a')] += 1 
            lst = tuple(lst)
            dic[lst].append(word)                                                   # d["a"].append(value) -> {a : value}
        return list(dic.values())
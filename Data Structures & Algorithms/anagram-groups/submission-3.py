class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        d = dict()
        finallist = []

        for i in strs:
            key = tuple(sorted(i))
            d.setdefault(key, []).append(i)

        for group in d.values():
            finallist.append(group)

        return finallist
class Solution:
    from collections import defaultdict
    from collections import Counter
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groupKey = tuple(sorted(Counter(s).items()))
            groups[groupKey].append(s)

        return list(groups.values())
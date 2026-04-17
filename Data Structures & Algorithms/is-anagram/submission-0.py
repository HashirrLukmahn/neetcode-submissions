from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        CountS = Counter(s)
        CountT = Counter(t)

        if CountS != CountT:
            return False
        

        return True
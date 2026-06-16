class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for c in s:
            freq[c] = freq.get(c,0) + 1

        for c in t:
            if c not in freq:
                return False

            freq[c] -= 1

            if freq[c] < 0:
                return False
            
        return True


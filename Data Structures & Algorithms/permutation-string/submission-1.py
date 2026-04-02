class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        i = 0
        while i+window_len<=len(s2):
            if sorted(s1)==sorted(s2[i:i+window_len]):
                return True
            i += 1
        return False
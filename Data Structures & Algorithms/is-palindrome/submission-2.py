class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l<r:
            print (l,r,s[l],s[r])
            while l<r and not s[l].isalnum():
                l = l + 1
            while r>l and not s[r].isalnum():
                r = r - 1
            if s[l]!=s[r]:
                return False
            
            l = l + 1
            r = r - 1    
        return True
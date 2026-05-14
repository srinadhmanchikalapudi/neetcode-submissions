class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()
        clean = l.replace(" ","")
        n = ''.join(ch for ch in clean if ch.isalnum()) # Removes special charecters from a string.
        m = len(n)
        
        for i in range(m//2):
            if n[i] == n[m-1-i]:
                continue
            else:
                print(n)
                return False
            
        return True
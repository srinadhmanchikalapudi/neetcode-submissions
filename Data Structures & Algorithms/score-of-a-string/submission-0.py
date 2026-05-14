class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(0,(len(s)-1)):
            d = ord(s[i])
            e = ord(s[i+1])
            count += abs(e - d)
    
        return count
        
        
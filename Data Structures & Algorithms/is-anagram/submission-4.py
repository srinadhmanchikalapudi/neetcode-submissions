class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        
        if(len(s) != len(t)):
            return False
        else:
            for i in s:
                if(i in s1):
                    s1[i] += 1
                else:
                    s1[i] = 0
            for j in t:
                if(j in t1):
                    t1[j] += 1 
                else:
                    t1[j] = 0
        return s1 == t1

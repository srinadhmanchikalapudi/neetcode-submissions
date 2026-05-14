class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s2 = 0
        t2 = 0
        s3 = list(s)
        t3 = list(t)
        if(len(s) != len(t)):
            return False
        else:
            for i in s:
                if (i in t3 and i in s3):
                    t3.remove(i)
                    s3.remove(i)
                else:
                    return False
        return t3 == s3
        

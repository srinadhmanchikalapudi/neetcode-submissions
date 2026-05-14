class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digits) ** 2 for digits in str(n))
        
        if n == 1:
            return True
        else:
            return False



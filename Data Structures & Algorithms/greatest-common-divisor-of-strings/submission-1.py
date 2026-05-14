class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        else:
            a = len(str1)
            b = len(str2)
            def gcd(a: int, b: int) -> int:
                while b != 0:
                    a,b = b, a%b
                return a

            gcd_len = gcd(a,b)
            return str1[:gcd_len]

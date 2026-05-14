class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        st = ""
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-indexed system
            remainder = columnNumber % 26
            st = chr(65 + remainder) + st  # 65 = 'A'
            columnNumber //= 26
        return st
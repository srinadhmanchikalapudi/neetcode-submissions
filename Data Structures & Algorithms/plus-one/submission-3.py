class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = len(digits)
        carry = 1
        for i in range(len(digits) -1, -1, -1): #does the same job as digits[::-1]
            digits[i] += carry
                        
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            elif digits[i] <= 9:
                carry = 0
                break

        if carry == 1:
            digits.insert(0,1)
            carry = 0

        return digits
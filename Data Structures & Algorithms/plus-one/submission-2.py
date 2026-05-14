class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = len(digits)
        digits = digits[::-1]
        carry = 1
        for i,elem in enumerate(digits):
            digits[i] += carry
                        
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            elif digits[i] <= 9:
                carry = 0
                break

        if carry == 1:
            digits.append(carry)
            carry = 0

        return digits[::-1]
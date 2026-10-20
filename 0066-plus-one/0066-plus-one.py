class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        r = len(digits) - 1
        carry = 1

        while r >= 0 and carry:
            sum = digits[r] + carry
            digits[r] = sum % 10 
            carry = sum //  10

            r -= 1

        if carry:
            digits.insert(0,carry)
        return digits

        
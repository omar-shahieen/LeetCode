class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts=0
        while left != right:
            right >>=1
            left >>=1
            shifts +=1 
        return left << shifts
        
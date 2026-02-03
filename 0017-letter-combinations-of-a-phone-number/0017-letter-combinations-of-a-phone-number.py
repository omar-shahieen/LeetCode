class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {
                '2': "abc",
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': "tuv",
                '9': "wxyz"
            }

        k = len(digits)
        path = []
        res = []

        def backtrack(idx):
            if len(path) == k :
                res.append("".join(path))
                return 

            letters = num_to_letters[ digits[idx]]

            for letter in letters :
                path.append(letter)
                backtrack(idx + 1)
                path.pop()

        
        backtrack(0)

        return res 

        

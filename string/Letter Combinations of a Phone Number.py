#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#SOLUTION:   queue
class Solution(object):
    def digitToChar(self, n):
        base = 96
        out = []
        #m : number of chars each digit represents
        #bias: the number of chars before the current digit
        if (n == 7):
            m = 5
            bias = (n - 2) * 3
        elif (n == 8):
            m = 4
            bias = (n - 3) * 3 + 4
        elif (n == 9):
            m = 5
            bias = (n - 3) * 3 + 4
        else:
            m = 4
            bias = (n - 2) * 3
        for i in range(1, m):
            out.append(chr(base + i + bias))
        return out

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        q = []
        for i in range(len(digits)):
            newQ = []
            cur = self.digitToChar(int(digits[i]))
            if (len(q) > 0):
                for ch in cur:
                    for elem in q:
                        newStr = elem + ch
                        newQ.append(newStr)
            else:
                for ch in cur:
                    newQ.append(ch)
            q = newQ
        return q

#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
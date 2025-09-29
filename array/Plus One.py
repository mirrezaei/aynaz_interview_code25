class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1
        carry = 1
        while (i >= 0 and carry > 0):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp / 10
            i -= 1
        if (carry > 0):
            digits = digits[::-1]
            digits.append(carry)
            digits = digits[::-1]
        return digits
#2025
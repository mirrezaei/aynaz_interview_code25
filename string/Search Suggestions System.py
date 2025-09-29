#Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

#Return list of lists of the suggested products after each character of searchWord is typed.

#Solution:
#1)first soort the product list
#2)then search the searchword chars in the prod list using a the binary search (increase number of chars step by step: search one char, two chars, three chars)

class Solution(object):
    count = 0

    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        def binarySearch(s):
            l = 0
            r = len(products) - 1
            k = len(s)
            found = -1
            while (l <= r):
                m = (l + r) / 2
                if products[m][:k] == s:
                    found = m
                    r = m - 1
                elif products[m][:k] < s:
                    l = m + 1
                else:
                    r = m - 1
            return found

        products.sort()
        out = []
        for i in range(len(searchWord)):
            ind = binarySearch(searchWord[:i + 1])# search the first i chars of searchword in prod list
            if ind == -1:
                out.append([])
            else:
                out.append([products[ind + j] for j in range(3) if (ind + j < len(products) and products[ind + j][:i + 1]==searchWord[:i + 1])])
        return out

s=Solution()

pp=["nn","bags","baggage","banner","box","cloths"]
ss="bags"
print(s.suggestedProducts(pp,ss))
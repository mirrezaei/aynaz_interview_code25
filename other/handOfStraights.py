#Alice has a hand of cards, given as an array of integers.

#Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

#Return true if and only if she can.

from collections import Counter

#optimal solution is sorting and convert it to a linked list-> time complexity: O n(log n)
#time complexity the following solution: n^2/W:  n/w interval, each one O(n) to find the min
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if (len(hand) % W != 0):
            return False
        else:
            d = Counter(hand)
            while (len(d) > 0):
                m = min(d)
                for i in range(m, m + W):
                    if (i not in d):
                        return False
                    else:
                        d[i] -= 1
                        if (d[i] == 0):
                            del d[i]
        return True

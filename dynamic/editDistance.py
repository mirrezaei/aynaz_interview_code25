#Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

#You have the following 3 operations permitted on a word:

#Insert a character
#Delete a character
#Replace a character

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(1, len(word2) + 1):
            m[0][i] = m[0][i - 1] + 1
        for j in range(1, len(word1) + 1):
            m[j][0] = m[j - 1][0] + 1

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if (word1[i - 1] == word2[j - 1]):
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = 1 + min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1])
        print(m)

        return m[len(word1)][len(word2)]

w1="horse"
w2="ros"
s=Solution()
print(s.minDistance(w1,w2))

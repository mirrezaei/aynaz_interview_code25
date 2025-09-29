class Solution(object):
    def search(self, c, s):
        seen = set()
        q = 2 ** 60 - 1
        d = 26
        h = pow(d, c) % q
        hash = 0
        i = c
        for j in range(c):
            hash = (d * hash + ord(s[j])) % q
        if (hash not in seen):
            seen.add(hash)
        for i in range(c, len(s)):
            hash = (d * hash - ord(s[i - c]) * h + ord(s[i])) % q
            if (hash not in seen):
                seen.add(hash)
            else:
                return c
        return 0

    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = 0
        r = len(S)
        o = 0
        while (l <= r):
            c = l + ((r - l) / 2)
            f = self.search(c, S)
            if (f == 0):
                r = c - 1
            else:
                l = c + 1
                o = f
        return o

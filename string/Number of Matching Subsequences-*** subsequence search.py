#Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
#Input:
#S = "abcde"
#words = ["a", "bb", "acd", "ace"]
#Output: 3
# the tri solution may not work well here, because as we go forward in the s string we need to save the pointers to different nodes of the trie.
# the best solution is to creat a trie with only one level and update it after processing each character in the s string
#dict:  key: current char, val: rest of string  [cur_char:]
#start to traverse the S and keep the state of each string in a dict
class Solution(object):
    def updateTrie(self, d, s):
        if (s[0] not in d):
            d[s[0]] = []
        if (len(s) > 1):
            d[s[0]].append(s[1:])
        else:
            d[s[0]].append("#")

    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            self.updateTrie(d, w)
        print(d)
        nu = 0
        for i in range(len(S)):
            if (S[i] in d):
                tmp = d[S[i]]
                del d[S[i]]
                for w in tmp:
                    if (w != "#"):
                        self.updateTrie(d, w)
                    else:
                        nu += 1
        return nu





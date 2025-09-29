#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

#Note:
#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.

class Solution(object):
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        out=set()
        def check(inp,curr):
            if inp=="":
                out.add(curr.lstrip())
            for i in range(len(s)):
                if inp[:i+1] in wordDict:
                    check(inp[i+1:],curr+" "+inp[:i+1])
        check(s,"")

        return list(out)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def check(inp):
            res=set()
            if inp in wordDict:
                res.add(inp)
            for i in range(len(s)):
                if inp[:i+1] in wordDict:
                    right=check(inp[i+1:])
                    for elem in right:
                        if elem!="":
                            res.add(inp[:i+1]+" "+elem)
            return res

        return list(check(s))


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
ss=Solution()
print(ss.wordBreak(s,wordDict))
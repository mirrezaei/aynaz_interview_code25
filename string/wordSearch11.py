#Given a 2D board and a list of words from the dictionary, find all words in the board.

#Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

#************************
#idea
#create a trie from the list of words, from each elemnt of the board we need to search those that are consistent with the trie
#the trie helps us to avoid the extra effort for searching the words that have the same prefix
#if we don't use the trie, we need to search for all the words from each entry of the board

class Solution(object):
    def trie(self, words):
        d = {}
        for w in words:
            t = d
            for ch in w:
                if (ch not in t):
                    t[ch] = {}

                t=t[ch]
            t["#"] = "#"  # end of word
        return d

    def find(self, board, i, j, out, path, d):
        if ("#" in d):
            out.add(path)
        if (i >= len(board) or i<0 or j<0 or  j >= len(board[0]) or (board[i][j] not in d) or board[i][j] == "@"):
            return
        cur = board[i][j]

        if (cur in d):
            board[i][j] = "@"
            self.find(board, i + 1, j, out, path + cur, d[cur])
            self.find(board, i, j + 1, out, path + cur, d[cur])
            self.find(board, i, j - 1, out, path + cur, d[cur])
            self.find(board, i - 1, j, out, path + cur, d[cur])
            board[i][j] = cur

    def findWords(self, board, words):#BEST
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        d = self.trie(words)
        out = set()
        for i in range(len(board)):# for each entry in the board, we should check which of the words may starts with.
            for j in range(len(board[i])):
                self.find(board, i, j, out, "", d)
        print(out)
        return out

board=[["a","b"],["c","d"]]
words=["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]

#board=[["a","b"],["c","d"]]
#words=["acdb"]
#board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#words=["oath","pea","eat","rain"]
s=Solution()
s.findWords(board, words)
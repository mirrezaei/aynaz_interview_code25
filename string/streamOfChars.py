#Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.
#For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for w in words:
            cur = self.d
            for ch in w:
                if (ch not in cur):
                    cur[ch] = {}
                cur = cur[ch]
            cur["#"] = None
        self.arr = []
        print(self.d)

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.arr.append(self.d)
        found = False
        tmp=[]
        for dic in self.arr:
            if (letter in dic):
                tmp.append(dic[letter])
                if ("#" in dic[letter]):
                    found = True
        return True if found else False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
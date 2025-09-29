"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def __init__(self, ):
        self.cur = []

    def read(self, buf, n):
        i = 0
        while (n > 0):
            if (len(self.cur) > 0):
                buf[i] = self.cur.pop(0)
                n -= 1
                i += 1
            else:#read and add to the queue
                b = [''] * 4
                c = read4(b)
                self.cur.extend(b[:c])
                if (c == 0):#there is nothing to read
                    return i
        return i



    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        if (len(self.cur) > 0):
            while (len(self.cur) > 0 and n > 0):
                buf[i] = self.cur.pop(0)
                i += 1
                n -= 1
        while (n > 0):
            b = [' '] * 4
            c = read4(b)
            if (c == 0):
                return max(0, i)
            t = n
            for j in range(c):
                if (j < t):
                    buf[i] = b[j]
                    i += 1
                    n -= 1
                else:
                    self.cur.append(b[j])
            if (c < 4):
                return i
        return i






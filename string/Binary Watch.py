class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        d = {0: 1, 1: 2, 2: 4, 3: 8, 4: 1, 5: 2, 6: 4, 7: 8, 8: 16, 9: 32}
        out = set()

        def toStr(hh, mm):
            hh = str(hh)
            mm = str(mm)
            if (len(mm) == 1):
                mm = "0" + mm
            out.add(hh + ":" + mm)
        # i refers to the bit number of the watch
        #i<4 referes to hour
        #i>4 referres to the min
        def rec(i, rem, h, m):
            if(rem==0):
                toStr(h, m)
            else:
                if (i < 10):
                    if (i < 4):
                        if(h + d[i]<12):#ith bit of hour
                            rec(i + 1, rem - 1, h + d[i], m)
                    else:
                        if(m + d[i]<60):#ith bit of min
                            rec(i + 1, rem - 1, h, m + d[i])
                    rec(i + 1, rem, h, m)# non of them


        if (num > 0 and num < 10):
            rec(0, num, 0, 0)
            print(out)
            return list(out)
        elif (num == 0):
            return ["0:00"]
        else:
            return None

s=Solution()
s.readBinaryWatch(1)
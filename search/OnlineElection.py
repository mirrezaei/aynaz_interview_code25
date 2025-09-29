class TopVotedCandidate(object):# this approach works but it is silly considering the time complexity, because at each time step, I keep the number of votes for all the candidate. Then I find the appropriate time step regarding the query and the calculate the winner
    #however; we can precomute the winner at each time step, find the appropriate time step regarding the query and return the winner

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.ti_per = []
        a = {}
        a[persons[0]] = [1, 0]
        self.ti_per.append(a)

        for i in range(1, len(persons)):
            self.ti_per.append({})
            if persons[i] not in self.ti_per[i - 1].keys():
                self.ti_per[i][persons[i]] = [1, i]

            for p in self.ti_per[i - 1].keys():
                self.ti_per[i][p] = [0, 0]
                if (p == persons[i]):
                    self.ti_per[i][p][0] = self.ti_per[i - 1][p][0] + 1
                    self.ti_per[i][p][1] = i
                else:
                    self.ti_per[i][p][0] = self.ti_per[i - 1][p][0]
                    self.ti_per[i][p][1] = self.ti_per[i - 1][p][1]

    def binarySearch(self, l, r, t):
        if (l == r):
            if (t >= self.times[l]):
                return l
            else:
                return None
        if (r == l + 1):
            if (t >= self.times[r]):
                return r
            elif (t >= self.times[l] and t < self.times[r]):
                return l
            else:
                return None
        else:
            m = (l + r) / 2
            if (self.times[m] == t):
                return m
            elif (t > self.times[m]):
                return self.binarySearch(m, r, t)
            else:
                return self.binarySearch(l, m - 1, t)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ind = self.binarySearch(0, len(self.times) - 1, t)
        maxVote = 0
        out = []
        for p in self.ti_per[ind].keys():
            if (self.ti_per[ind][p][0] > maxVote):
                out = []
                maxVote = self.ti_per[ind][p][0]
                out.append(p)
            elif (self.ti_per[ind][p][0] == maxVote):
                out.append(p)
        if (len(out) == 1):
            return out[0]
        else:
            recent = -1
            for p in out:
                if (self.ti_per[ind][p][1] > recent):
                    recent = self.ti_per[ind][p][1]
                    final = p
            return final


class TopVotedCandidate2(object): #this approach works much faster than previous. At each time step, we only need to keep the leader and the nimber of its votes

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.ti_per = []
        self.vote = {}
        self.ti_per.append((persons[0], 1))
        self.vote[persons[0]] = 1
        for i in range(1, len(persons)):
            if (persons[i] not in self.vote.keys()):
                self.vote[persons[i]] = 1
            else:
                self.vote[persons[i]] += 1
            if (self.vote[persons[i]] >= self.ti_per[i - 1][1]):
                self.ti_per.append((persons[i], self.vote[persons[i]]))
            else:
                self.ti_per.append(self.ti_per[i - 1])

    def binarySearch(self, l, r, t):
        while (l < r):
            m = (l + r) / 2
            if self.times[m] == t:
                return m
            elif t < self.times[m]:
                r = m
            else:
                l = m + 1
        return l - 1

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ind = self.binarySearch(0, len(self.times) - 1, t)
        return self.ti_per[ind][0]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
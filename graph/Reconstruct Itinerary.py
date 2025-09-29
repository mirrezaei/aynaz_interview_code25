#Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

from collections import defaultdict
from copy import deepcopy
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        d = defaultdict(list)
        for t in tickets:
            if (t[0] not in d):
                d[t[0]] = []
            d[t[0]].append(t[1])

        path = ["JFK"]

        def dfs(node):
            if(len(path)==len(tickets)+1):
                return True
            else:
                targetList=deepcopy(sorted(d[node]))
                for cur in targetList:
                    d[node].remove(cur)
                    path.append(cur)
                    finished=dfs(cur)
                    if(finished!=True):
                        path.pop(-1)
                        d[node].append(cur)
                    else:
                        return True

        dfs("JFK")

        print(path)
        return path





#Input= [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Input= [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#Input=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
Input=[["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
Input=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s=Solution()
s.findItinerary(Input)

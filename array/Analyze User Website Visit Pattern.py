from collections import defaultdict
from collections import Counter


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        dweb = defaultdict(set)
        duser = defaultdict(list)
        for i in range(len(username)):
            duser[username[i]].append((website[i], timestamp[i]))
        for key in duser:
            tmp = sorted(duser[key], key=lambda x: x[1])
            duser[key] = [web[0] for web in tmp]
        for key in duser:
            for i in range(len(duser[key])):
                for j in range(i + 1, len(duser[key])):
                    for k in range(j + 1, len(duser[key])):
                        web = duser[key][i] + " " + duser[key][j] + " " + duser[key][k]
                        dweb[web].add(key)

        maxCount = 0
        res = []
        for key in dweb:
            if (len(dweb[key] )> maxCount):
                maxCount = len(dweb[key])
                res = [key]
            elif (len(dweb[key]) == maxCount):
                res.append(key)
        print(res)
        res = sorted(res)[0]
        res = res.split(" ")
        return res

class Solution2(object):# not verified on leetcode
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        users=defaultdict(list)
        pattern=defaultdict(set)
        for i in range(len(username)):
            users[username[i]].append((timestamp[i],website[i]))
        for user in users:
            users[user].sort(key=lambda x: x[0])
        for user in users:
            for i in range(len(users[user])):
                for j in range(i+1,len(users[user])):
                    for k in range(j+1,len(users[user])):
                        pattern[users[user][i][1]+" "+users[user][j][1]+" "+users[user][k][1]].add(user)

        result=[]
        maxCount=0
        for pat in pattern:
            if len(pattern[pat])>maxCount:
                result=pat.split(" ")
                maxCount=len(pattern[pat])
        return result


s=Solution()
username=["dowg","dowg","dowg"]
timestamp=[158931262,562600350,148438945]
website=["y","loedo","y"]


username=["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
timestamp=[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
website=["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
print(s.mostVisitedPattern(username, timestamp, website))


#2025
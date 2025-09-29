#Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

#Example:
#Given a / b = 2.0, b / c = 3.0.
#queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
#return [6.0, 0.5, -1.0, 1.0, -1.0 ].

#The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

#According to the example above:
from __future__ import division
import numpy as np
import collections

class Solution(object):
    def calcEquation(self, equations, values, queries):# this approach doesn't work correctly because ***** loop can only retrive relations with one intermediate stop, not more. for example a->b->c->d; this code cannot find elation between a and d
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        chars = {}
        i = 0
        for e in equations:#find all possible characters
            for c in e:
                if (c not in chars.keys()):
                    chars[c] = i
                    i += 1

        m = np.full((len(chars.keys()),len(chars.keys())), -1.0)
        for i in range(len(m)):# matrix diameter
            m[i][i] = 1
        for i, e in enumerate(equations):#matrix symmetric
            m[chars[e[0]], chars[e[1]]] = values[i]
            m[chars[e[1]],chars[e[0]]] = 1/values[i]

        for i in range(len(m)):#inference
            for j in range(len(m)):
                if (m[i][j] == -1):
                    for k in range(len(m[i])): # ********************
                        if ( k != i and m[k][j] != -1 and m[i][k]!=-1):
                            m[i][j] = m[i][k] * m[k][j]
                            m[j][i] = 1/(m[i][k] * m[k][j])

                            break
        out=[]
        for q in queries:
            if(q[0] in chars.keys() and q[1] in chars.keys()):
                m1=chars[q[0]]
                m2=chars[q[1]]
                out.append(m[m1,m2])
            else:
                out.append(-1)
        print(out)
        return out
    def dfs(self,g,f,l):
        stack=[]
        visited=set()
        stack.append((f,1))
        visited.add(f)
        while(len(stack)>0):
            cur=stack.pop(-1)
            l_child=g[cur[0]]
            cal=cur[-1]
            for ch in l_child:
                if(ch[0] not in visited):
                    stack.append((ch[0],ch[1]*cal))
                    visited.add(ch[0])
            if(cur[0]==l):
                return cal
        return -1.0


    def calcEquation2(self, equations, values, queries): #DFS approach
        g=collections.defaultdict(list)
        for e,v in zip(equations,values):  # find all possible characters
           g[e[0]].append((e[1],v))
           g[e[1]].append((e[0],1/v))

        m=np.full((len(g.keys()),len(g.keys())),-1.0)
        for i in range(len(m)):# matrix diameter
            m[i][i] = 1
        i=0
        chars=collections.defaultdict()
        for e in equations:#find all possible characters
            for c in e:
                if (c not in chars.keys()):
                    chars[c] = i
                    i += 1
        for i, e in enumerate(equations):#matrix symmetric
            m[chars[e[0]], chars[e[1]]] = values[i]
            m[chars[e[1]],chars[e[0]]] = 1/values[i]

        out = []
        for q in queries:
            if (q[0] in chars.keys() and q[1] in chars.keys()):
                m1 = chars[q[0]]
                m2 = chars[q[1]]
                if(m[m1, m2]!=-1):
                    out.append(m[m1, m2])
                else:
                    res=self.dfs(g,q[0],q[1])
                    if(res!=-1):
                        m[m1, m2] = res
                        m[m2,m1]=1/res
                    out.append(res)
            else:
                out.append(-1)
        print(out)
        return out






s=Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

equations =[["a","e"],["b","e"]]
values = [4.0,3.0]
queries =[["a","b"],["e","e"],["x","x"]]
#s.calcEquation(equations,values,queries)
s.calcEquation2(equations,values,queries)

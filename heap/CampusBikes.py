import heapq
class Solution(object):
    def manhattan(self, x1, x2):
        return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

    def assignBikes2(self, workers, bikes):# the first solution is brute force and passes all test cases. Time complexity : O(mnlog(mn))
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        #m: number of bikes
        #n:number of people
        t = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                t.append([self.manhattan(workers[i], bikes[j]), i, j])
        t = sorted(t, key=lambda x: (x[0], x[1], x[2]))
        # print(t)
        w = [-1 for i in range(len(workers))]
        bSet = set()
        for i in range(len(t)):
            if (w[t[i][1]] == -1):
                if (t[i][2] not in bSet):
                    w[t[i][1]] = t[i][2]
                    bSet.add(t[i][2])
        print(w)
        return w

    def assignBikes(self, workers, bikes):# this solution is much faster. time complexity: O(nmlog(m))+ O(nlog(n))+ O(nmlog(n))=  O(nm(log(n)+log(m)))
        #nmlog(m)  : find the distance of all bikes from each person (nm) and sort them nmlog(m)
        #nlog(n)  : create heap for n workers
        #nmlog(n) : heap maintenance

        wo=[]
        for i in range(len(workers)):
            temp=[]
            for j in range(len(bikes)):
                temp.append([self.manhattan(workers[i], bikes[j]),i, j])
            wo.append(temp)

        for i in range(len(wo)):
            wo[i]=sorted(wo[i],key=lambda x: (x[0], x[1],x[2]))

        h=[]#minheap
        for i in range(len(wo)):
            heapq.heappush(h,wo[i][0])
            del wo[i][0]

        bSet = set()
        w = [-1 for i in range(len(workers))]

        while(len(h)>0):
            e=heapq.heappop(h)
            if(e[2] not in bSet):
                w[e[1]]=e[2]
                bSet.add(e[2])
            else:
                heapq.heappush(h,wo[e[1]][0])
                del wo[e[1]][0]

        print(w)
        return w









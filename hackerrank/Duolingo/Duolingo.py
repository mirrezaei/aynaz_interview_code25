
def findGroupIndex(studentSet,stNu):
    for j,stuSet in enumerate(studentSet):
        if stNu in stuSet:
            return j
def getTheGroups(n, queryType, students1, students2):
        studentSet=[]
        totalList=[]
        for i in range(n):
            studentSet.append(set())
            studentSet[i].add(i+1)

        for i,query in enumerate(queryType):
            if(query=="Friend"):
                in1=findGroupIndex(studentSet,students1[i])
                in2=findGroupIndex(studentSet,students2[i])

                studentSet[in1]=studentSet[in1].union(studentSet[in2])
                del studentSet[in2]

            else:
                in1 = findGroupIndex(studentSet, students1[i])
                in2 = findGroupIndex(studentSet, students2[i])
                total=len(studentSet[in1])+len(studentSet[in2])
                totalList.append(total)

        return totalList







print(getTheGroups(10,["Friend","Friend","Friend","Total","Friend","Friend","Friend","Total"],[1,1,3,1,7,6,9,6],[2,4,5,2,8,9,10,9]))
# print(getTheGroups(4,["Friend","Friend","Total"],[1,2,1],[2,3,4]))


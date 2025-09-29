#A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

#Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):# this approach works but has memory problem
        #a[i][j]=a[i-sy-j][j]  or a[i][j-sx-i]
        if tx - sx<0 or ty - sy<0:
            return False
        a = [[False] * (tx - sx + 1) for i in range(ty - sy + 1)]
        a[0][0] = True
        # a[j][0]=sx
        j = 0
        while (j < len(a[0])):
            a[0][j] = True
            j = j + sy
        j = 0
        while (j < len(a)):
            a[j][0] = True
            j = j + sx
        for i in range(1, len(a)):
            for j in range(1, len(a[0])):
                if (i - sx-j >=0  and a[i - sx-j][j]):
                    a[i][j] = True
                if (j - sy-i >= 0 and a[i][j - sy-i]):
                    a[i][j] = True
        print(a)
        return a[len(a)-1][len(a[0])-1]
    #idea is to determine if we can cover the distance of  tx - sx  and ty - sy by steps of
    #a[i][j]: if we can traverse the distance of i and j from origin by steps sx and sy respectively; i efers to y and j refers to x


    def reachingPoints2(self, sx, sy, tx, ty):# this approach doesn't have memory problem, but it has time  problem

        vis = set()
        def search2(x, y):
            if (x, y) in vis: return
            if x > tx or y > ty: return
            vis.add((x, y))
            search2(x + y, y)
            search2(x, x + y)
        search2(sx, sy)
        if((tx,ty) in vis):
            return True
        else:
            return False

    def reachingPoints3(self, sx, sy, tx, ty):#backward, but it still has time  problem

        def search2(x, y):
            if (x, y)==(sx,sy):
                return True
            elif(x>=0 and y>=0):
                search2(x-y,y)
                search2(x,y-x)
        search2(tx,ty)

        return True if search2(sx, sy) else False






s=Solution()
sx=9
sy=5
tx=12
ty=8

sx = 1
sy = 1
tx = 3
ty = 5

sx=9
sy=10
tx=9
ty=19

#sx=1
#sy=8
#tx=4
#ty=15

sx=10
sy=2
tx=2
ty=11

#sx=6
#sy=5
#tx=11
#ty=16


sx=3
sy=3
tx=12
ty=9

sx=35
sy=13
tx=455955547
ty=420098884

print(s.reachingPoints3(sx, sy, tx, ty))


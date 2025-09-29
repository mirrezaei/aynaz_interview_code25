from collections import defaultdict

#A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

#the idea is that we start from the left side and update the end variable for current split based on current char.
#There are 3 cases:
#1) create a new partiotion: only if we have generated a split using the last index, update the end no matter what
#2) extend the current partiotion
#3)save the current partiotion:
class Solution(object):
    def partitionLabels(self, S):
        d = defaultdict(int)
        for i in range(len(S)):
            d[S[i]] = i
        out = []
        begin = -1
        end = -1#possible end for current partition
        update = True
        for i in range(len(S)):
            if (update):#create a new partiotion: only if we have generated a split using the last index, update the end no matter what
                end = d[S[i]]
                update = False
            if (i < end):#possible extend the partiotion
                if (d[S[i]] > end):#generally we updadte end only if the current char has a larger end,
                    end = d[S[i]]
            else:#save the current partiotion: create a split and remember to update end next iteration
                out.append(end - begin)
                begin = end
                update = True
        return out

S = "ababcbacadefegdehijhklij"
so=Solution()
print(so.partitionLabels2(S))

#2025
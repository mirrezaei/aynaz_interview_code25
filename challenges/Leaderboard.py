#!/bin/python3

import math
import os
import random
import re
import sys

#Climbing the Leaderboard
#Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

#The player with the highest score is ranked number  on the leaderboard.
#Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
#For example, the four players on the leaderboard have high scores of , , , and . Those players will have ranks , , , and , respectively. If Alice's scores are ,  and , her rankings after each game are ,  and .

#Function Description

#Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element represents Alice's rank after the  game.

#climbingLeaderboard has the following parameter(s):

#scores: an array of integers that represent leaderboard scores
#alice: an array of integers that represent Alice's scores
#Input Format

#The first line contains an integer , the number of players on the leaderboard.
#The next line contains  space-separated integers , the leaderboard scores in decreasing order.
#The next line contains an integer, , denoting the number games Alice plays.
#The last line contains  space-separated integers , the game scores.

#Constraints

# for
# for
#The existing leaderboard, , is in descending order.
#Alice's scores, , are in ascending order.
#Subtask

#For  of the maximum score:

#Output Format

#Print  integers. The  integer should indicate Alice's rank after playing the  game.

#Sample Input 1

#7
#100 100 50 40 40 20 10
#4
#5 25 50 120

#Sample Output 1

#6
#4
#2
#1

# Complete the climbingLeaderboard function below.
def binarySearch(scores,elem):
    if(len(scores)==1):
        if(scores[0]==elem):
            return 0,scores[0]
        elif(elem>scores[0]):
            return 1,scores[0]
        else:
            return -1,scores[0]
    else:
        mid=int(len(scores)/2)
        if(scores[mid]==elem):
            return 0,scores[mid]
        elif(elem>scores[mid]):
            #if(mid-1<=0):
            #    return binarySearch(scores[0],elem)
            #else:
            return binarySearch(scores[0:mid],elem)
        else:
            if(mid+1>=len(scores)):
                return binarySearch(scores[-1:],elem)
            else:
                return binarySearch(scores[mid+1:],elem)

def assignScore(scores):
    ranks={}
    scoreInd=1
    for score in scores:
        if score not in ranks.keys():
            ranks[score]=scoreInd
            scoreInd=scoreInd+1
    return ranks


def climbingLeaderboard2(scores, alice):# this approach is using a binary search and has time computationally problems
    res=[]
    ranks=assignScore(scores)
    for alice_score in alice:
        status,elem=binarySearch(scores,alice_score)
        if(status==0):
            res.append(ranks[elem])
        elif(status==1):
            res.append(ranks[elem])
        else:
            res.append(ranks[elem]+1)
    return res

def climbingLeaderboard(scores, alice): # this approach is more efficeint
    res=[]
    ranks=assignScore(scores)
    index=[i for i in range(len(alice))]
    com=list(zip(alice,index))
    com=sorted(com,key=lambda elements:elements[0],reverse=True)
    i=0
    rankFound=False
    endList=False
    for j,elem in enumerate(com):
        if (endList == False):
            while (rankFound == False):
                if elem[0] == scores[i]:
                    res.append((elem[1], ranks[scores[i]]))
                    rankFound = True
                elif elem[0] > scores[i]:
                    res.append((elem[1], ranks[scores[i]]))
                    rankFound = True
                else:
                    i = i + 1
                    if (i >= len(scores)):
                        endList = True
                        break
            rankFound = False

        if (endList == True):
            lastScore = ranks[scores[-1]]
            if elem[0] == scores[-1]:
                res.append((elem[1], lastScore))
            else:
                res.append((elem[1], lastScore + 1))

    final=[0 for i in range(len(alice))]
    for i in range(len(alice)):
        final[res[i][0]]=res[i][1]
    return final



if __name__ == '__main__':
    fptr = open("results.txt", 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

import collections

from collections import Counter

def split(sent):
    arr=sent.split(" ")
    arr=Counter(arr)
    dict=sorted(arr.items(), key=lambda x: x[1],reverse=True)
    print(dict)
    enumerate

sen="I have a a great"
split(sen)
#Stream: backiuwcatbeforewerehpqojf
#Input: ["back", "before", "cat", "fore", "were", "for"]
##Output: [0, 10, 7, 12, 16, 12]
#Generator: char getNextChar();
from collections import defaultdict
def trie(inp):
    d={}
    for w in  inp:
        cur=d
        for ch in w:
            if(ch not  in cur):
                cur[ch]={}
            cur=cur[ch]
        cur["#"]=None
    return d
# the idea is that we create a trie from the list of words (input)
#then we process the stream chars one by one
#we have a queue that has pointers to the locations of the trie that so far we have found mathces .
# when we process one char from the stream we should review all the pointers in the queue in case we can continue them
def main():
    stream= "backiuwcatbeforewerehpqojf"
    input=["back", "before", "cat", "fore", "were", "for"]
    d=trie(input)
    arr=[(d,"")]
    out={}
    for j,ch in enumerate(stream):
        i=0
        while(i<len(arr)):#pointers to the trie
            dic=arr[i][0]
            if("#" in dic):
                out[arr[i][1]]=j-len(arr[i][1])#replcae the word with straing index
            if ch not in dic:
                arr.pop(i)
            else:
                arr[i]=(dic[ch],arr[i][1]+ch)
                i+=1
        arr.append((d,""))
    print(out)

main()


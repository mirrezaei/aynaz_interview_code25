#This problem is an interactive problem new to the LeetCode platform.

#We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

#You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

#This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

#For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

#Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import numpy as np
import random
import collections
import itertools
class Solution2(object):
    def guess(self,w,sec):
        count=0
        for i in range(len(sec)):
            if(sec[i]==w[i]):
                count+=1
        return count

    def match(self,w1,w2):
        return sum(c1==c2 for c1,c2 in zip(w1,w2))

    def findSecretWord(self, wordlist, secret):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        countGuess=0
        while len(wordlist)>0:
            ct={}# the same as  count
            for w1 in wordlist:
                counter=0
                for w2 in wordlist:
                    if(w1!=w2):
                        if(self.match(w1,w2)==0):
                            counter+=1
                ct[w1]=counter

            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            wg = min(wordlist, key=lambda w: count[w])#this is the min part #the idea is to select a word that gives us a shorter list  of worlist.
            # we can make the wordlist shorter if we select a word that has more matches. so, we compute the number of 0 matches for each word.
            #it means that for word w we compute how many words there exists that there is no match in characers between them and the word w
            # then we select the word with minimum 0 matches, with the hope that it has more matches with others

            #in my opinion, another approach is that instead of choosing the word with minimum 0 matches, select the word that has maximum number of matches

            #j=random.randint(0,len(wordlist)-1)
            #wg = wordlist[j]

            g = self.guess(wg, secret)
            countGuess+=1
            if (g == 6):
                    print(countGuess)
                    print(wg)
                    break
            wordlist=[w for w in wordlist if(sum(i==j for i,j in zip(w,wg)))==g] #  this is the maximum part# the secret word should have exactly g matches with wg



secret="hbaczn"
words=["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

#secret="cymplm"
#words=["eykdft","gjeixr","eksbjm","mxqhpk","tjplhf","ejgdra","npkysm","jsrsid","cymplm","vegdgt","jnhdvb","jdhlzb","sgrghh","jvydne","laxvnm","xbcliw","emnfcw","pyzdnq","vzqbuk","gznrnn","robxqx","oadnrt","kzwyuf","ahlfab","zawvdf","edhumz","gkgiml","wqqtla","csamxn","bisxbn","zwxbql","euzpol","mckltw","bbnpsg","ynqeqw","uwvqcg","hegrnc","rrqhbp","tpfmlh","wfgfbe","tpvftd","phspjr","apbhwb","yjihwh","zgspss","pesnwj","dchpxq","axduwd","ropxqf","gahkbq","yxudiu","dsvwry","ecfkxn","hmgflc","fdaowp","hrixpl","czkgyp","mmqfao","qkkqnz","lkzaxu","cngmyn","nmckcy","alpcyy","plcmts","proitu","tpzbok","vixjqn","suwhab","dqqkxg","ynatlx","wmbjxe","hynjdf","xtcavp","avjjjj","fmclkd","ngxcal","neyvpq","cwcdhi","cfanhh","ruvdsa","pvzfyx","hmdmtx","pepbsy","tgpnql","zhuqlj","tdrsfx","xxxyle","zqwazc","hsukcb","aqtdvn","zxbxps","wziidg","tsuxvr","florrj","rpuorf","jzckev","qecnsc","rrjdyh","zjtdaw","dknezk"]

s=Solution2()
s.findSecretWord(words,secret)
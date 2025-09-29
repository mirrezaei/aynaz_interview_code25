import itertools

#Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of words the expression represents.

#Grammar can best be understood through simple examples:


class Solution(object):
    def braceExpansionII(self, expression):
        # the idea is that at each level we keep one concat and one prod
        #concat shows the elements that can be concated with the next ones
        #prod shows the elements that can be producted with the next ones
        #when we see "{" then we save the prod and cocat that we obtained until here in stack
        #when we see "}" then we pop old prod and old concat from stack. Find the product of old prod and (cur prod+ cur concat) as the cur prod and update the concat with the old concat
        inp=expression
        prod=[]
        concat=[]
        stack=[]#the current array we consider for prod calculation
        for i in range(len(inp)):
            if(inp[i]=="{"):# it is time to save the potential chars for prod or concat
                stack.append(concat)
                stack.append(prod)
                concat = []
                prod = []
            elif(inp[i]=="}"):#
                preProd=stack.pop()
                preConcat=stack.pop()
                tmp=[]
                for elem in preProd or [""]:# we can compute the production for preProd and current (concat+prod)
                    for c in concat+prod:
                        tmp.append(elem+c)
                prod=tmp
                concat=preConcat#concat doesn't change
            elif (inp[i].isalpha()):#if we see an alphabet we first assume it as a prod potential, unless we see the ","
                prod=[c + inp[i] for c in prod or [""]]
            elif (inp[i] == ","):# if we see "," we transfer prod to concat
                concat+=prod
                prod=[]
        return sorted(set(concat+prod))

s=Solution()
inp="{a,b,c,e}{c{d,e}}"
print(s.braceExpansionII(inp))

#Single letters represent a singleton set containing that word.
#R("a") = {"a"}
#R("w") = {"w"}
#When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
#R("{a,b,c}") = {"a","b","c"}
#R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
#When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
#R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
#R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
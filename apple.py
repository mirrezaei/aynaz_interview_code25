d={
	'rule1':['born', 'head_quarter'],
	'rule2': {'marriage':['marriage', 'sex_with']}
}
triples=[('Obama', 'born', 'Hawaei'),('Obama', 'born', 'Honololu'),('Mike','marriage','Leila'),('Mike', 'sex_with', 'looleh'),('Jafar','marriage','Leila'),('Jafar', 'marriage', 'looleh')]


def check():
    contradict={}
    for k in d['rule2']:
        if(k not in contradict):
            contradict[k]=set()
        for r in d['rule2'][k]:
            if(r not in contradict):
                contradict[r]=set()
            contradict[r].add(k)
            contradict[k].add(r)



    facts={}
    for t in triples:
        if(t[0] not in facts):
            facts[t[0]]={}
        if(t[1] not in facts[t[0]]):
            facts[t[0]][t[1]]=t[2]
        if(t[1] in contradict):
            con=contradict[t[1]]
            for r in con:
                if(r in facts[t[0]] and facts[t[0]][r]!=facts[t[0]][t[1]]):
                    return False
    return True

print(check())

def add(q1,q2,b):
    s1=q1[::-1]
    s2=q2[::-1]
    i=0
    carry=0
    out=""
    while(i<min(len(s1),len(s2))):
        sum=carry+int(s1[i])+int(s2[i])
        m=sum/b
        r=sum%b
        out+=str(r)
        carry=m
        i+=1
    if(carry!=0):
        s=s1 if len(s1)>len(s2) else s2
        while(i<len(s)):
            sum=carry+int(s[i])
            carry=sum/b
            r=sum%b
            out+=str(r)
            i+=1
        out+=str(carry) if carry!=0 else ""
    else:
        if(len(s1)>len(s2)):
            out+=s1[i:]
        else:
            out+=s2[i:]

    return out[::-1]


print(add("222","1222",3))